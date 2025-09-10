from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_HEALTH_STATUS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_health_status")
        print(f"Uploaded {data.num_rows} rows to health_status")
        
    save_state("health_status", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
