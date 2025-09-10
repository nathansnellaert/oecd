from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_REAC_EMP@DF_CARE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_personal_care_workers")
        print(f"Uploaded {data.num_rows} rows to personal_care_workers")
        
    save_state("personal_care_workers", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
