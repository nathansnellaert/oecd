#!/usr/bin/env python3
"""
Process a single OECD dataset by code.
Designed to be called as a subprocess to avoid memory issues.
"""
import os
import sys
import argparse
from datetime import datetime
from utils import upload_data, save_state, validate_environment
from general import fetch_data

def process_dataset(dataset_code: str) -> None:
    """
    Process and upload a single OECD dataset.
    
    Args:
        dataset_code: The OECD dataset identifier (e.g., "DSD_TAXBEN_SBE@DF_SBE")
    """
    # Fetch the data
    print(f"Fetching dataset {dataset_code}...")
    data = fetch_data(dataset_code)
    
    if data.num_rows == 0:
        print(f"No data found for {dataset_code}")
        return
    
    # Generate dataset name from code (simplified version)
    # Remove DSD_ prefix and @DF_ parts, lowercase
    dataset_name = dataset_code.replace("DSD_", "").split("@")[0].lower()
    
    # Upload the data
    print(f"Uploading {data.num_rows:,} rows...")
    upload_data(data, dataset_name)
    
    # Save state
    save_state(dataset_name, {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows,
        "dataset_code": dataset_code
    })
    
    print(f"✓ Successfully processed {dataset_code}: {data.num_rows:,} rows")

def main():
    parser = argparse.ArgumentParser(description='Process a single OECD dataset')
    parser.add_argument('dataset_code', type=str, help='OECD dataset code (e.g., DSD_TAXBEN_SBE@DF_SBE)')
    parser.add_argument('--dataset-name', type=str, help='Optional custom name for the dataset')
    
    args = parser.parse_args()
    
    # Set up environment
    os.environ['CONNECTOR_NAME'] = 'oecd'
    if not os.environ.get('RUN_ID'):
        os.environ['RUN_ID'] = f'dataset-{args.dataset_code}-{datetime.now().strftime("%Y%m%d%H%M%S")}'
    
    validate_environment()
    
    try:
        if args.dataset_name:
            # If custom name provided, use it
            print(f"Processing {args.dataset_code} as {args.dataset_name}...")
            data = fetch_data(args.dataset_code)
            
            if data.num_rows > 0:
                upload_data(data, args.dataset_name)
                save_state(args.dataset_name, {
                    "last_updated": datetime.now().isoformat(),
                    "row_count": data.num_rows,
                    "dataset_code": args.dataset_code
                })
                print(f"✓ Successfully processed {args.dataset_code}: {data.num_rows:,} rows")
            else:
                print(f"No data found for {args.dataset_code}")
        else:
            process_dataset(args.dataset_code)
            
    except Exception as e:
        print(f"✗ Failed to process {args.dataset_code}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()