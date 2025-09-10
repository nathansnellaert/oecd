from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FFS@DF_FFS_DNK")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_fossil_fuel_support_denmark")
        print(f"Uploaded {data.num_rows} rows to fossil_fuel_support_denmark")
        
    save_state("fossil_fuel_support_denmark", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
