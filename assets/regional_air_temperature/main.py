from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_CLIM@DF_AIR_TEMP")
    
    if data.num_rows > 0:
        upload_data(data, "regional_air_temperature")
        print(f"Uploaded {data.num_rows} rows to regional_air_temperature")
        
    save_state("regional_air_temperature", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
