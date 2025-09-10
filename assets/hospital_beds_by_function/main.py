from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_REAC_HOSP@DF_BEDS_FUNC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_hospital_beds_by_function")
        print(f"Uploaded {data.num_rows} rows to hospital_beds_by_function")
        
    save_state("hospital_beds_by_function", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
