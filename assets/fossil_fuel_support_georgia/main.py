from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FFS@DF_FFS_GEO")
    
    if data.num_rows > 0:
        upload_data(data, "fossil_fuel_support_georgia")
        print(f"Uploaded {data.num_rows} rows to fossil_fuel_support_georgia")
        
    save_state("fossil_fuel_support_georgia", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
