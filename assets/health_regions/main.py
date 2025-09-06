from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_HEALTH@DF_HEALTH")
    
    if data.num_rows > 0:
        upload_data(data, "health_regions")
        print(f"Uploaded {data.num_rows} rows to health_regions")
        
    save_state("health_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
