from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B5")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_informal_workers_gender_household")
        print(f"Uploaded {data.num_rows} rows to informal_workers_gender_household")
        
    save_state("informal_workers_gender_household", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
