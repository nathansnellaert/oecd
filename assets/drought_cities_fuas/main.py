from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_CLIM@DF_DROUGHT")
    
    if data.num_rows > 0:
        upload_data(data, "drought_cities_fuas")
        print(f"Uploaded {data.num_rows} rows to drought_cities_fuas")
        
    save_state("drought_cities_fuas", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
