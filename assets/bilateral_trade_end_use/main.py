from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BTIGE@DF_BTIGE")
    
    if data.num_rows > 0:
        upload_data(data, "bilateral_trade_end_use")
        print(f"Uploaded {data.num_rows} rows to bilateral_trade_end_use")
        
    save_state("bilateral_trade_end_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
