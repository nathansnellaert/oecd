from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AIR_POL@DF_AIR_POLL")
    
    if data.num_rows > 0:
        upload_data(data, "air_pollution_exposure")
        print(f"Uploaded {data.num_rows} rows to air_pollution_exposure")
        
    save_state("air_pollution_exposure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
