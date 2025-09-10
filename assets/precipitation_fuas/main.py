from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_CLIM@DF_PRECIP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_precipitation_fuas")
        print(f"Uploaded {data.num_rows} rows to precipitation_fuas")
        
    save_state("precipitation_fuas", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
