from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_TERR@DF_DENSITY")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_population_buildup_density_cities_fua")
        print(f"Uploaded {data.num_rows} rows to population_buildup_density_cities_fua")
        
    save_state("population_buildup_density_cities_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
