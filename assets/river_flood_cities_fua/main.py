from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_CLIM@DF_RIVER_FLOOD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_river_flood_cities_fua")
        print(f"Uploaded {data.num_rows} rows to river_flood_cities_fua")
        
    save_state("river_flood_cities_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
