from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ECH@FIRE_THREAT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_wildfire_exposure")
        print(f"Uploaded {data.num_rows} rows to wildfire_exposure")
        
    save_state("wildfire_exposure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
