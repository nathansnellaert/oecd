from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10_IDC@DF_TABLE9A_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_annual_fixed_assets_by_asset")
        print(f"Uploaded {data.num_rows} rows to annual_fixed_assets_by_asset")
        
    save_state("annual_fixed_assets_by_asset", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
