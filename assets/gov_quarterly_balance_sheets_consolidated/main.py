from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T710GOV_Q")
    
    if data.num_rows > 0:
        upload_data(data, "gov_quarterly_balance_sheets_consolidated")
        print(f"Uploaded {data.num_rows} rows to gov_quarterly_balance_sheets_consolidated")
        
    save_state("gov_quarterly_balance_sheets_consolidated", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
