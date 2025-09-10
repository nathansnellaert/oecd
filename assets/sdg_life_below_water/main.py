from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG_G_14")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sdg_life_below_water")
        print(f"Uploaded {data.num_rows} rows to sdg_life_below_water")
        
    save_state("sdg_life_below_water", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
