from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE12")
    
    if data.num_rows > 0:
        upload_data(data, "annual_government_accounts")
        print(f"Uploaded {data.num_rows} rows to annual_government_accounts")
        
    save_state("annual_government_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
