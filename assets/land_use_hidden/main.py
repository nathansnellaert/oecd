from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LAND_USE_HID@DF_LAND_USE_HID")
    
    if data.num_rows > 0:
        upload_data(data, "land_use_hidden")
        print(f"Uploaded {data.num_rows} rows to land_use_hidden")
        
    save_state("land_use_hidden", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
