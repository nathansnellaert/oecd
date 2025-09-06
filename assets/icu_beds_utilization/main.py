from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_REAC_HOSP@DF_BEDS_ICU")
    
    if data.num_rows > 0:
        upload_data(data, "icu_beds_utilization")
        print(f"Uploaded {data.num_rows} rows to icu_beds_utilization")
        
    save_state("icu_beds_utilization", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
