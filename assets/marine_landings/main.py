from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FISH_PROD@DF_FISH_LAND")
    
    if data.num_rows > 0:
        upload_data(data, "marine_landings")
        print(f"Uploaded {data.num_rows} rows to marine_landings")
        
    save_state("marine_landings", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
