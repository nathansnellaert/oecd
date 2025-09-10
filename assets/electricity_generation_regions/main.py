from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ENE@DF_PROD_ELEC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_electricity_generation_regions")
        print(f"Uploaded {data.num_rows} rows to electricity_generation_regions")
        
    save_state("electricity_generation_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
