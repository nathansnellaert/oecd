from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_COMPEMP@DF_GOV_COMPEMP_2025")
    
    if data.num_rows > 0:
        upload_data(data, "gov_central_admin_employment")
        print(f"Uploaded {data.num_rows} rows to gov_central_admin_employment")
        
    save_state("gov_central_admin_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
