from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FISH_PROD@DF_FISH_AQUA")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_aquaculture_production")
        print(f"Uploaded {data.num_rows} rows to aquaculture_production")
        
    save_state("aquaculture_production", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
