from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TRENDS@DF_TRENDSSAFETY")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_road_safety")
        print(f"Uploaded {data.num_rows} rows to road_safety")
        
    save_state("road_safety", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
