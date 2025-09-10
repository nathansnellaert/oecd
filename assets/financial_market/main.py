from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STES@DF_FINMARK")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_financial_market")
        print(f"Uploaded {data.num_rows} rows to financial_market")
        
    save_state("financial_market", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
