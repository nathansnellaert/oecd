from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_HOSP_DISCHARGE")
    
    if data.num_rows > 0:
        upload_data(data, "hospital_discharges")
        print(f"Uploaded {data.num_rows} rows to hospital_discharges")
        
    save_state("hospital_discharges", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
