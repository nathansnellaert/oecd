from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_ENV_GREEN_AREA_DDOWN@DF_GREEN_AREA_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_green_areas")
        print(f"Uploaded {data.num_rows} rows to local_green_areas")
        
    save_state("local_green_areas", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
