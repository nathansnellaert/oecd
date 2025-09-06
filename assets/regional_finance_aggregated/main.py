from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SNGF_AGG@DF_REGOFI")
    
    if data.num_rows > 0:
        upload_data(data, "regional_finance_aggregated")
        print(f"Uploaded {data.num_rows} rows to regional_finance_aggregated")
        
    save_state("regional_finance_aggregated", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
