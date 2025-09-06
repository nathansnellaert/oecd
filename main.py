import os
os.environ['CONNECTOR_NAME'] = 'oecd'
os.environ['RUN_ID'] = os.getenv('RUN_ID', 'local-run')

import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime
from utils import validate_environment, load_state

def get_all_datasets():
    """Get all dataset codes from asset directories"""
    datasets = []
    assets_dir = Path(__file__).parent / "assets"
    
    for asset_dir in sorted(assets_dir.iterdir()):
        if not asset_dir.is_dir():
            continue
        
        main_file = asset_dir / "main.py"
        if not main_file.exists():
            continue
            
        # Extract dataset code from main.py
        try:
            with open(main_file, 'r') as f:
                content = f.read()
            
            # Look for fetch_data("...") pattern
            import re
            match = re.search(r'fetch_data\(["\']([^"\']+)["\']\)', content)
            if match:
                dataset_code = match.group(1)
                dataset_name = asset_dir.name
                datasets.append((dataset_code, dataset_name))
        except:
            continue
    
    return datasets

def process_dataset_subprocess(dataset_code: str, dataset_name: str) -> bool:
    """
    Process a dataset in a subprocess to avoid memory issues.
    
    Returns:
        True if successful, False otherwise
    """
    cmd = [
        sys.executable,
        "process_dataset.py",
        dataset_code,
        "--dataset-name", dataset_name
    ]
    
    try:
        # Run in subprocess with memory constraints
        result = subprocess.run(
            cmd,
            cwd=Path(__file__).parent,
            capture_output=True,
            text=True,
            timeout=1800  # 30 minute timeout per dataset
        )
        
        # Print subprocess output
        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print(f"✗ Timeout processing {dataset_code}")
        return False
    except Exception as e:
        print(f"✗ Error processing {dataset_code}: {e}")
        return False

def main():
    validate_environment()
    
    # Load external reference dataflows to skip
    external_ref_dataflows = set()
    dataflows_path = Path(__file__).parent / "defs" / "dataflows.json"
    if dataflows_path.exists():
        with open(dataflows_path, 'r') as f:
            dataflows = json.load(f)
        for df in dataflows:
            if df.get("isExternalReference") == "true":
                external_ref_dataflows.add(df.get("id"))
    
    print(f"Found {len(external_ref_dataflows)} external reference dataflows to skip")
    
    # Get all datasets
    all_datasets = get_all_datasets()
    print(f"Found {len(all_datasets)} total datasets")
    
    # Filter out external references and check state
    datasets_to_process = []
    skipped_datasets = []
    up_to_date_datasets = []
    
    for dataset_code, dataset_name in all_datasets:
        # Skip external references
        if dataset_code in external_ref_dataflows:
            skipped_datasets.append((dataset_name, "external reference"))
            continue
        
        # Check state
        state = load_state(dataset_name)
        if state and 'last_updated' in state:
            last_updated = datetime.fromisoformat(state['last_updated'])
            days_ago = (datetime.now() - last_updated).days
            if days_ago < 30:
                up_to_date_datasets.append((dataset_name, days_ago))
                continue
        
        datasets_to_process.append((dataset_code, dataset_name))
    
    # Print summary
    print(f"\n📊 Dataset Status Summary:")
    print(f"  ✓ Up-to-date (< 30 days): {len(up_to_date_datasets)}")
    print(f"  ⏳ To process: {len(datasets_to_process)}")
    print(f"  ⚠️  Skipped: {len(skipped_datasets)}")
    
    if up_to_date_datasets:
        print(f"\n✓ Recently updated datasets:")
        for name, days in sorted(up_to_date_datasets, key=lambda x: x[1])[:10]:
            print(f"  - {name} ({days} days ago)")
        if len(up_to_date_datasets) > 10:
            print(f"  ... and {len(up_to_date_datasets) - 10} more")
    
    if not datasets_to_process:
        print("\n✅ All datasets are up to date!")
        return
    
    print(f"\n🚀 Processing {len(datasets_to_process)} datasets...")
    
    # Process each dataset in a subprocess
    successful = []
    failed = []
    
    for i, (dataset_code, dataset_name) in enumerate(datasets_to_process, 1):
        print(f"\n[{i}/{len(datasets_to_process)}] Processing {dataset_name}...")
        
        success = process_dataset_subprocess(dataset_code, dataset_name)
        
        if success:
            successful.append(dataset_name)
        else:
            failed.append(dataset_name)
        
        # Small delay between datasets to avoid overwhelming the API
        import time
        time.sleep(5)
    
    # Print final summary
    print("\n" + "="*50)
    print("📊 OECD Connector Summary")
    print("="*50)
    
    if successful:
        print(f"\n✅ Successfully processed {len(successful)} datasets")
    
    if failed:
        print(f"\n❌ Failed to process {len(failed)} datasets:")
        for name in failed[:10]:
            print(f"  - {name}")
        if len(failed) > 10:
            print(f"  ... and {len(failed) - 10} more")
    
    if up_to_date_datasets:
        print(f"\n⏭️ Skipped {len(up_to_date_datasets)} up-to-date datasets")
    
    print("\n✨ OECD connector run complete!")

if __name__ == "__main__":
    main()