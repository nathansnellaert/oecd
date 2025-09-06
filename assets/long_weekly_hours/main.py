from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HW@DF_LNG_WK_HRS")
    
    if data.num_rows > 0:
        upload_data(data, "long_weekly_hours")
        print(f"Uploaded {data.num_rows} rows to long_weekly_hours")
        
    save_state("long_weekly_hours", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
