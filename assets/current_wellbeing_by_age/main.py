from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HSL@DF_HSL_CWB_AGE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_current_wellbeing_by_age")
        print(f"Uploaded {data.num_rows} rows to current_wellbeing_by_age")
        
    save_state("current_wellbeing_by_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
