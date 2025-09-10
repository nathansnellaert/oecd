from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC1@DF_QSA")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quarterly_sector_accounts")
        print(f"Uploaded {data.num_rows} rows to quarterly_sector_accounts")
        
    save_state("quarterly_sector_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
