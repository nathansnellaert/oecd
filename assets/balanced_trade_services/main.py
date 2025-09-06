from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BATIS@DF_BATIS")
    
    if data.num_rows > 0:
        upload_data(data, "balanced_trade_services")
        print(f"Uploaded {data.num_rows} rows to balanced_trade_services")
        
    save_state("balanced_trade_services", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
