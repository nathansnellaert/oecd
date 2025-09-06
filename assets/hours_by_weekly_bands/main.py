from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HW@DF_USL_WK_HRS")
    
    if data.num_rows > 0:
        upload_data(data, "hours_by_weekly_bands")
        print(f"Uploaded {data.num_rows} rows to hours_by_weekly_bands")
        
    save_state("hours_by_weekly_bands", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
