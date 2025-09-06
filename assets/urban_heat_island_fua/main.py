from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_ENV@DF_UHI")
    
    if data.num_rows > 0:
        upload_data(data, "urban_heat_island_fua")
        print(f"Uploaded {data.num_rows} rows to urban_heat_island_fua")
        
    save_state("urban_heat_island_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
