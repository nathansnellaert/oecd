from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_CLIM@DF_LAND_TEMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_land_temperature")
        print(f"Uploaded {data.num_rows} rows to regional_land_temperature")
        
    save_state("regional_land_temperature", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
