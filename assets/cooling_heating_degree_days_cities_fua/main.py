from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_ENER@DF_CDD_HDD")
    
    if data.num_rows > 0:
        upload_data(data, "cooling_heating_degree_days_cities_fua")
        print(f"Uploaded {data.num_rows} rows to cooling_heating_degree_days_cities_fua")
        
    save_state("cooling_heating_degree_days_cities_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
