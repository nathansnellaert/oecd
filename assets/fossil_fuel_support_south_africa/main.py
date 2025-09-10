from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FFS@DF_FFS_ZAF")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_fossil_fuel_support_south_africa")
        print(f"Uploaded {data.num_rows} rows to fossil_fuel_support_south_africa")
        
    save_state("fossil_fuel_support_south_africa", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
