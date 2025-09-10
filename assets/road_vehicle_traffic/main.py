from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ST@DF_STTRAFFIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_road_vehicle_traffic")
        print(f"Uploaded {data.num_rows} rows to road_vehicle_traffic")
        
    save_state("road_vehicle_traffic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
