from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_SCREEN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_health_screening")
        print(f"Uploaded {data.num_rows} rows to health_screening")
        
    save_state("health_screening", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
