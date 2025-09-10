from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_WAITING")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_healthcare_waiting_times")
        print(f"Uploaded {data.num_rows} rows to healthcare_waiting_times")
        
    save_state("healthcare_waiting_times", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
