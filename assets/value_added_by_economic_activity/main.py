from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE6")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_value_added_by_economic_activity")
        print(f"Uploaded {data.num_rows} rows to value_added_by_economic_activity")
        
    save_state("value_added_by_economic_activity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
