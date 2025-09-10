from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_AGWATER")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_water_use")
        print(f"Uploaded {data.num_rows} rows to water_use")
        
    save_state("water_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
