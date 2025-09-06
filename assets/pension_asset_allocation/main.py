from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FP@DF_WI")
    
    if data.num_rows > 0:
        upload_data(data, "pension_asset_allocation")
        print(f"Uploaded {data.num_rows} rows to pension_asset_allocation")
        
    save_state("pension_asset_allocation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
