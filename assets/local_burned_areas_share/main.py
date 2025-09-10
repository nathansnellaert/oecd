from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_FIRE_DDOWN@DF_FIRE_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_burned_areas_share")
        print(f"Uploaded {data.num_rows} rows to local_burned_areas_share")
        
    save_state("local_burned_areas_share", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
