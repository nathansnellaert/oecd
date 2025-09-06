from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_AGWQ")
    
    if data.num_rows > 0:
        upload_data(data, "agricultural_water_quality")
        print(f"Uploaded {data.num_rows} rows to agricultural_water_quality")
        
    save_state("agricultural_water_quality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
