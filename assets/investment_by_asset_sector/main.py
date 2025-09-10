from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE14_GFCF")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_investment_by_asset_sector")
        print(f"Uploaded {data.num_rows} rows to investment_by_asset_sector")
        
    save_state("investment_by_asset_sector", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
