from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_WFMI@DF_HEALTH_WFMI")
    
    if data.num_rows > 0:
        upload_data(data, "health_workforce_migration")
        print(f"Uploaded {data.num_rows} rows to health_workforce_migration")
        
    save_state("health_workforce_migration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
