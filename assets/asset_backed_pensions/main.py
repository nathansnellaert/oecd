from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FP@DF_FPS")
    
    if data.num_rows > 0:
        upload_data(data, "asset_backed_pensions")
        print(f"Uploaded {data.num_rows} rows to asset_backed_pensions")
        
    save_state("asset_backed_pensions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
