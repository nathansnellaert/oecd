from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_ASSET_ACCOUNTS@DF_WATER_ASSET_ACCOUNTS")
    
    if data.num_rows > 0:
        upload_data(data, "water_asset_accounts")
        print(f"Uploaded {data.num_rows} rows to water_asset_accounts")
        
    save_state("water_asset_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
