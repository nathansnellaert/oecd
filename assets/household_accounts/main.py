from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG@DF_NAAG_V")
    
    if data.num_rows > 0:
        upload_data(data, "household_accounts")
        print(f"Uploaded {data.num_rows} rows to household_accounts")
        
    save_state("household_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
