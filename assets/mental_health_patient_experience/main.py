from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_MHPREM")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_mental_health_patient_experience")
        print(f"Uploaded {data.num_rows} rows to mental_health_patient_experience")
        
    save_state("mental_health_patient_experience", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
