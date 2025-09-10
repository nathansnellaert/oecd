from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HW@DF_AVG_USL_WK_WKD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_weekly_hours_main_job")
        print(f"Uploaded {data.num_rows} rows to weekly_hours_main_job")
        
    save_state("weekly_hours_main_job", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
