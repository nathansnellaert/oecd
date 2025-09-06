from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ENV@DF_AIR_POLLUT")
    
    if data.num_rows > 0:
        upload_data(data, "air_pollution_exposure_regions")
        print(f"Uploaded {data.num_rows} rows to air_pollution_exposure_regions")
        
    save_state("air_pollution_exposure_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
