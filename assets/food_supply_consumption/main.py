from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_LVNG@DF_HEALTH_LVNG_FSC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_food_supply_consumption")
        print(f"Uploaded {data.num_rows} rows to food_supply_consumption")
        
    save_state("food_supply_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
