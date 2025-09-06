from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T720R_A")
    
    if data.num_rows > 0:
        upload_data(data, "annual_balance_sheets_non_consolidated")
        print(f"Uploaded {data.num_rows} rows to annual_balance_sheets_non_consolidated")
        
    save_state("annual_balance_sheets_non_consolidated", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
