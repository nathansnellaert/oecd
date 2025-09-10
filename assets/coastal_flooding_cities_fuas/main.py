from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_CLIM@DF_COASTAL_FLOOD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_coastal_flooding_cities_fuas")
        print(f"Uploaded {data.num_rows} rows to coastal_flooding_cities_fuas")
        
    save_state("coastal_flooding_cities_fuas", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
