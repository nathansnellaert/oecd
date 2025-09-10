from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FISH_PROD@DF_FISH_INLAND")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_inland_fisheries")
        print(f"Uploaded {data.num_rows} rows to inland_fisheries")
        
    save_state("inland_fisheries", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
