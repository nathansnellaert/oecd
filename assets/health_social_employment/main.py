from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_EMP_REAC@DF_SOC_EMPLOY")
    
    if data.num_rows > 0:
        upload_data(data, "health_social_employment")
        print(f"Uploaded {data.num_rows} rows to health_social_employment")
        
    save_state("health_social_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
