from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B13")
    
    if data.num_rows > 0:
        upload_data(data, "workers_health_insurance_formality")
        print(f"Uploaded {data.num_rows} rows to workers_health_insurance_formality")
        
    save_state("workers_health_insurance_formality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
