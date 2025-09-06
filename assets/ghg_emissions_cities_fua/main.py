from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_ENV@DF_GHG")
    
    if data.num_rows > 0:
        upload_data(data, "ghg_emissions_cities_fua")
        print(f"Uploaded {data.num_rows} rows to ghg_emissions_cities_fua")
        
    save_state("ghg_emissions_cities_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
