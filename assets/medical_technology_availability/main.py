from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_REAC_HOSP@DF_MED_TECH")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_medical_technology_availability")
        print(f"Uploaded {data.num_rows} rows to medical_technology_availability")
        
    save_state("medical_technology_availability", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
