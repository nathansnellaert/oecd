from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_AGLAND")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_agricultural_land_area")
        print(f"Uploaded {data.num_rows} rows to agricultural_land_area")
        
    save_state("agricultural_land_area", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
