from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG@DF_NAAG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_national_accounts_aggregates")
        print(f"Uploaded {data.num_rows} rows to national_accounts_aggregates")
        
    save_state("national_accounts_aggregates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
