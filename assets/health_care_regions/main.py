from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_HEALTH@DF_CARE")
    
    if data.num_rows > 0:
        upload_data(data, "health_care_regions")
        print(f"Uploaded {data.num_rows} rows to health_care_regions")
        
    save_state("health_care_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
