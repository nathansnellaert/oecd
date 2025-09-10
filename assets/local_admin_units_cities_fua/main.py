from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_TERR@DF_LAU")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_admin_units_cities_fua")
        print(f"Uploaded {data.num_rows} rows to local_admin_units_cities_fua")
        
    save_state("local_admin_units_cities_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
