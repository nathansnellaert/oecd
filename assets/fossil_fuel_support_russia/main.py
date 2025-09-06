from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FFS@DF_FFS_RUS")
    
    if data.num_rows > 0:
        upload_data(data, "fossil_fuel_support_russia")
        print(f"Uploaded {data.num_rows} rows to fossil_fuel_support_russia")
        
    save_state("fossil_fuel_support_russia", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
