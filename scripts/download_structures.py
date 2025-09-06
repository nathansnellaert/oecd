#!/usr/bin/env python3
"""Download all OECD data structure definitions (DSDs) and codelists"""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
import httpx
from collections import defaultdict
import time
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=1, period=1)  # 1 call per second - very conservative
def get_data_structure(base_url: str, agency_id: str, structure_id: str, version: str = "latest") -> dict:
    """Fetch a specific data structure definition"""
    try:
        response = httpx.get(
            f"{base_url}/datastructure/{agency_id}/{structure_id}/{version}",
            timeout=60.0
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            # Rate limited - wait and retry
            print(f"Rate limited for structure {structure_id}, waiting 10 seconds...")
            time.sleep(10)
            return get_data_structure(base_url, agency_id, structure_id, version)
        else:
            print(f"Failed to fetch structure {structure_id}: {e}")
            return None
    except Exception as e:
        print(f"Failed to fetch structure {structure_id}: {e}")
        return None
    
    root = ET.fromstring(response.text)
    namespaces = {
        "s": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
        "c": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common"
    }
    
    structure = {
        "id": structure_id,
        "agency_id": agency_id,
        "version": version,
        "dimensions": [],
        "attributes": [],
        "measures": [],
        "codelists": set()  # Track unique codelists
    }
    
    # Find the DataStructure element
    dsd = root.find(f".//s:DataStructure[@id='{structure_id}']", namespaces)
    if dsd is None:
        return None
    
    # Get components
    components = dsd.find(".//s:DataStructureComponents", namespaces)
    if components is not None:
        # Dimensions
        for dim in components.findall(".//s:DimensionList//s:Dimension", namespaces):
            dim_info = {
                "id": dim.get("id"),
                "position": dim.get("position"),
                "type": "Dimension"
            }
            
            # Get concept identity
            concept_ref = dim.find(".//s:ConceptIdentity//Ref", namespaces)
            if concept_ref is not None:
                dim_info["concept_id"] = concept_ref.get("id")
            
            # Get codelist reference
            codelist_ref = dim.find(".//s:LocalRepresentation//s:Enumeration//Ref", namespaces)
            if codelist_ref is not None:
                codelist_id = codelist_ref.get("id")
                codelist_agency = codelist_ref.get("agencyID", agency_id)
                dim_info["codelist"] = f"{codelist_agency}:{codelist_id}"
                structure["codelists"].add(f"{codelist_agency}:{codelist_id}")
            
            structure["dimensions"].append(dim_info)
        
        # Time dimension
        time_dim = components.find(".//s:DimensionList//s:TimeDimension", namespaces)
        if time_dim is not None:
            structure["dimensions"].append({
                "id": time_dim.get("id", "TIME_PERIOD"),
                "type": "TimeDimension"
            })
        
        # Attributes
        for attr in components.findall(".//s:AttributeList//s:Attribute", namespaces):
            attr_info = {
                "id": attr.get("id"),
                "assignmentStatus": attr.get("assignmentStatus"),
                "type": "Attribute"
            }
            
            # Get codelist reference
            codelist_ref = attr.find(".//s:LocalRepresentation//s:Enumeration//Ref", namespaces)
            if codelist_ref is not None:
                codelist_id = codelist_ref.get("id")
                codelist_agency = codelist_ref.get("agencyID", agency_id)
                attr_info["codelist"] = f"{codelist_agency}:{codelist_id}"
                structure["codelists"].add(f"{codelist_agency}:{codelist_id}")
            
            structure["attributes"].append(attr_info)
        
        # Measures
        for measure in components.findall(".//s:MeasureList//s:PrimaryMeasure", namespaces):
            structure["measures"].append({
                "id": measure.get("id"),
                "type": "PrimaryMeasure"
            })
    
    # Convert set to list for JSON serialization
    structure["codelists"] = list(structure["codelists"])
    
    return structure

@sleep_and_retry
@limits(calls=1, period=1)  # 1 call per second - very conservative
def get_codelist(base_url: str, agency_id: str, codelist_id: str, version: str = "latest") -> dict:
    """Fetch a specific codelist"""
    try:
        response = httpx.get(
            f"{base_url}/codelist/{agency_id}/{codelist_id}/{version}",
            timeout=30.0
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            # Rate limited - wait and retry
            print(f"Rate limited for codelist {agency_id}:{codelist_id}, waiting 10 seconds...")
            time.sleep(10)
            return get_codelist(base_url, agency_id, codelist_id, version)
        else:
            print(f"Failed to fetch codelist {agency_id}:{codelist_id}: {e}")
            return None
    except Exception as e:
        print(f"Failed to fetch codelist {agency_id}:{codelist_id}: {e}")
        return None
    
    root = ET.fromstring(response.text)
    namespaces = {
        "s": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
        "c": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common"
    }
    
    codes = {}
    for code in root.findall(".//s:Code", namespaces):
        code_id = code.get("id")
        # Get English name
        name_elem = None
        for name in code.findall(".//c:Name", namespaces):
            if name.get("{http://www.w3.org/XML/1998/namespace}lang") == "en":
                name_elem = name
                break
        
        if name_elem is not None:
            codes[code_id] = name_elem.text
        else:
            codes[code_id] = code_id
    
    return {
        "id": f"{agency_id}:{codelist_id}",
        "agency_id": agency_id,
        "codelist_id": codelist_id,
        "codes": codes
    }

def main():
    base_url = "https://sdmx.oecd.org/public/rest"
    
    # Load dataflows
    data_dir = Path(__file__).parent.parent / "defs"
    with open(data_dir / "dataflows.json", 'r') as f:
        dataflows = json.load(f)
    
    print(f"Processing {len(dataflows)} dataflows...")
    
    # Track unique structures and codelists
    structures = {}
    all_codelists = set()
    
    # Load existing structures if available (to resume)
    structures_file = data_dir / "structures.json"
    if structures_file.exists():
        print("Loading existing structures...")
        with open(structures_file, 'r') as f:
            structures = json.load(f)
        print(f"Loaded {len(structures)} existing structures")
        
        # Extract codelists from existing structures
        for structure in structures.values():
            all_codelists.update(structure.get("codelists", []))
    
    # Process each dataflow to get its structure
    for i, df in enumerate(dataflows):
        if i % 100 == 0:
            print(f"Progress: {i}/{len(dataflows)}")
        
        if not df.get("structure_id"):
            continue
        
        structure_key = f"{df['structure_agency_id']}:{df['structure_id']}:{df.get('structure_version', 'latest')}"
        
        # Skip if we already have this structure
        if structure_key in structures:
            continue
        
        # Fetch structure
        structure = get_data_structure(
            base_url,
            df["structure_agency_id"],
            df["structure_id"],
            df.get("structure_version", "latest")
        )
        
        if structure:
            structures[structure_key] = structure
            all_codelists.update(structure["codelists"])
    
    print(f"\nFound {len(structures)} unique structures")
    print(f"Found {len(all_codelists)} unique codelists")
    
    # Save structures
    structures_file = data_dir / "structures.json"
    with open(structures_file, 'w') as f:
        json.dump(structures, f, indent=2)
    print(f"Saved structures to {structures_file}")
    
    # Fetch all unique codelists
    print("\nFetching codelists...")
    codelists = {}
    
    # Load existing codelists if available (to resume)
    codelists_file = data_dir / "codelists.json"
    if codelists_file.exists():
        print("Loading existing codelists...")
        with open(codelists_file, 'r') as f:
            codelists = json.load(f)
        print(f"Loaded {len(codelists)} existing codelists")
    
    for i, cl_ref in enumerate(all_codelists):
        if i % 50 == 0:
            print(f"Progress: {i}/{len(all_codelists)}")
        
        # Skip if already downloaded
        if cl_ref in codelists:
            continue
            
        agency_id, codelist_id = cl_ref.split(":", 1)
        codelist = get_codelist(base_url, agency_id, codelist_id)
        
        if codelist:
            codelists[cl_ref] = codelist
            
        # Save progress every 100 codelists
        if i > 0 and i % 100 == 0:
            with open(codelists_file, 'w') as f:
                json.dump(codelists, f, indent=2)
            print(f"Saved progress: {len(codelists)} codelists")
    
    # Save codelists
    codelists_file = data_dir / "codelists.json"
    with open(codelists_file, 'w') as f:
        json.dump(codelists, f, indent=2)
    print(f"Saved {len(codelists)} codelists to {codelists_file}")
    
    # Print some statistics
    codelist_usage = defaultdict(int)
    for structure in structures.values():
        for cl in structure["codelists"]:
            codelist_usage[cl] += 1
    
    print("\nMost used codelists:")
    for cl, count in sorted(codelist_usage.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {cl}: used by {count} structures")

if __name__ == "__main__":
    main()