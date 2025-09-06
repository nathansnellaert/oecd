from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HW@DF_EMP_USL_WK_HRS")
    
    if data.num_rows > 0:
        upload_data(data, "employment_by_weekly_hours")
        print(f"Uploaded {data.num_rows} rows to employment_by_weekly_hours")
        
    save_state("employment_by_weekly_hours", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
