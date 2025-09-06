from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_SOIL_MOISTURE_DDOWN@DF_SOIL_MOISTURE_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "local_soil_moisture")
        print(f"Uploaded {data.num_rows} rows to local_soil_moisture")
        
    save_state("local_soil_moisture", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
