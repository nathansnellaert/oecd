from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LMP@DF_LMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_labour_market_programmes")
        print(f"Uploaded {data.num_rows} rows to labour_market_programmes")
        
    save_state("labour_market_programmes", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
