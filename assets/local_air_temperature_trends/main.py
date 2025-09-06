from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_AIR_TEMP_DDOWN@DF_AIR_TEMP_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "local_air_temperature_trends")
        print(f"Uploaded {data.num_rows} rows to local_air_temperature_trends")
        
    save_state("local_air_temperature_trends", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
