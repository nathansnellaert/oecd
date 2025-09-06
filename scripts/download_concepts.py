#!/usr/bin/env python3
"""Download all OECD concepts and save to defs directory"""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
import httpx

def extract_concepts(root):
    """Extract all concepts from the XML response"""
    namespaces = {
        "s": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure",
        "c": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common"
    }
    
    concepts = {}
    
    # Find all ConceptSchemes
    for scheme in root.findall(".//s:ConceptScheme", namespaces):
        scheme_id = scheme.get("id")
        scheme_agency = scheme.get("agencyID")
        
        # Process each Concept
        for concept in scheme.findall(".//s:Concept", namespaces):
            concept_id = concept.get("id")
            
            # Get names and descriptions
            names = {}
            descriptions = {}
            
            for name_elem in concept.findall(".//c:Name", namespaces):
                lang = name_elem.get("{http://www.w3.org/XML/1998/namespace}lang", "en")
                names[lang] = name_elem.text
            
            for desc_elem in concept.findall(".//c:Description", namespaces):
                lang = desc_elem.get("{http://www.w3.org/XML/1998/namespace}lang", "en")
                if desc_elem.text:
                    descriptions[lang] = desc_elem.text
            
            concepts[concept_id] = {
                "id": concept_id,
                "names": names,
                "name": names.get("en", names.get(list(names.keys())[0]) if names else concept_id),
                "descriptions": descriptions,
                "description": descriptions.get("en", ""),
                "scheme_id": scheme_id,
                "scheme_agency": scheme_agency
            }
    
    return concepts

def get_unique_agencies():
    """Extract unique agencies from dataflows.json"""
    data_dir = Path(__file__).parent.parent / "defs"
    dataflows_file = data_dir / "dataflows.json"
    
    if not dataflows_file.exists():
        print("Error: dataflows.json not found. Please run download_dataflows.py first.")
        return []
    
    with open(dataflows_file, 'r') as f:
        dataflows = json.load(f)
    
    # Extract unique agencies
    agencies = set()
    for df in dataflows:
        if df.get('agencyID'):
            agencies.add(df['agencyID'])
    
    # Filter for OECD-related agencies only
    oecd_agencies = [a for a in agencies if a.startswith('OECD')]
    
    return sorted(oecd_agencies)

def download_concepts_from_oecd_agencies():
    """Download concepts from OECD agencies with references"""
    base_url = "https://sdmx.oecd.org/public/rest"
    
    # Get all OECD agencies from dataflows
    oecd_agencies = get_unique_agencies()
    
    if not oecd_agencies:
        print("No OECD agencies found in dataflows.json")
        return {}
    
    print(f"Found {len(oecd_agencies)} OECD agencies in dataflows:")
    for agency in oecd_agencies:
        print(f"  - {agency}")
    
    all_concepts = {}
    
    for agency in oecd_agencies:
        try:
            print(f"Trying {agency} dataflows with references...")
            response = httpx.get(f"{base_url}/dataflow/{agency}/all/latest?references=all", timeout=120.0)
            
            if response.status_code == 200:
                root = ET.fromstring(response.text)
                concepts = extract_concepts(root)
                print(f"  Found {len(concepts)} concepts from {agency}")
                
                # Merge concepts
                for cid, cdata in concepts.items():
                    if cid not in all_concepts or (cdata.get("description") and not all_concepts[cid].get("description")):
                        all_concepts[cid] = cdata
            else:
                print(f"  HTTP {response.status_code} for {agency}")
                
        except Exception as e:
            print(f"  Error for {agency}: {type(e).__name__}: {str(e)}")
    
    return all_concepts

def main():
    # Create data directory
    data_dir = Path(__file__).parent.parent / "defs"
    data_dir.mkdir(exist_ok=True)
    
    # Download concepts from OECD agencies
    print("Downloading concepts with descriptions from OECD agencies...")
    concepts = download_concepts_from_oecd_agencies()
    
    if concepts:
        print(f"\nTotal concepts collected: {len(concepts)}")
        
        # Count concepts with descriptions
        with_desc = sum(1 for c in concepts.values() if c.get("description"))
        print(f"Concepts with descriptions: {with_desc}")
        
        # Save concepts
        concepts_file = data_dir / "concepts.json"
        with open(concepts_file, 'w') as f:
            json.dump(concepts, f, indent=2)
        print(f"Saved concepts to {concepts_file}")
        
        # Show examples
        print("\nExample concepts with descriptions:")
        examples = [c for c in concepts.values() if c.get("description")][:10]
        for concept in examples:
            print(f"\n{concept['id']}: {concept['name']}")
            print(f"  {concept['description'][:100]}...")

if __name__ == "__main__":
    main()