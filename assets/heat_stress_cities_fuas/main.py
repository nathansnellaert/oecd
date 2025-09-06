from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_CLIM@DF_HEAT_STRESS")
    
    if data.num_rows > 0:
        upload_data(data, "heat_stress_cities_fuas")
        print(f"Uploaded {data.num_rows} rows to heat_stress_cities_fuas")
        
    save_state("heat_stress_cities_fuas", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
