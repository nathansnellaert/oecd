from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SNGF_DISAGG@DF_REGOFI")
    
    if data.num_rows > 0:
        upload_data(data, "regional_finance_disaggregated")
        print(f"Uploaded {data.num_rows} rows to regional_finance_disaggregated")
        
    save_state("regional_finance_disaggregated", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
