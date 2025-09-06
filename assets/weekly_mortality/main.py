from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_MORTALITY@DF_MORTALITY")
    
    if data.num_rows > 0:
        upload_data(data, "weekly_mortality")
        print(f"Uploaded {data.num_rows} rows to weekly_mortality")
        
    save_state("weekly_mortality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
