from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_USE@DF_WATER_USE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_freshwater_use")
        print(f"Uploaded {data.num_rows} rows to freshwater_use")
        
    save_state("freshwater_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
