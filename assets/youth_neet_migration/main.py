from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_TRANS_MIGR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_youth_neet_migration")
        print(f"Uploaded {data.num_rows} rows to youth_neet_migration")
        
    save_state("youth_neet_migration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
