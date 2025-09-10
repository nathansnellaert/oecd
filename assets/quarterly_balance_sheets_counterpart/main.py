from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T725R_Q")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quarterly_balance_sheets_counterpart")
        print(f"Uploaded {data.num_rows} rows to quarterly_balance_sheets_counterpart")
        
    save_state("quarterly_balance_sheets_counterpart", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
