from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG_G_15")
    
    if data.num_rows > 0:
        upload_data(data, "sdg_life_on_land")
        print(f"Uploaded {data.num_rows} rows to sdg_life_on_land")
        
    save_state("sdg_life_on_land", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
