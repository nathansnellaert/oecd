from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_ENV_LAND_COVER_DDOWN@DF_LAND_COVER_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_land_cover")
        print(f"Uploaded {data.num_rows} rows to local_land_cover")
        
    save_state("local_land_cover", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
