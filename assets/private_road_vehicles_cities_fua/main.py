from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_SOC@DF_VEH")
    
    if data.num_rows > 0:
        upload_data(data, "private_road_vehicles_cities_fua")
        print(f"Uploaded {data.num_rows} rows to private_road_vehicles_cities_fua")
        
    save_state("private_road_vehicles_cities_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
