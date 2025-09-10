from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_HOSP_AV_LENGTH")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_hospital_stay_length")
        print(f"Uploaded {data.num_rows} rows to hospital_stay_length")
        
    save_state("hospital_stay_length", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
