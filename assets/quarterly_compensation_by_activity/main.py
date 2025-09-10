from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN1@DF_QNA_BY_ACTIVITY_COE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quarterly_compensation_by_activity")
        print(f"Uploaded {data.num_rows} rows to quarterly_compensation_by_activity")
        
    save_state("quarterly_compensation_by_activity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
