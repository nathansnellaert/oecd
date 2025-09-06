from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_RESOURCES@DF_WATER_RESOURCES")
    
    if data.num_rows > 0:
        upload_data(data, "freshwater_resources")
        print(f"Uploaded {data.num_rows} rows to freshwater_resources")
        
    save_state("freshwater_resources", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
