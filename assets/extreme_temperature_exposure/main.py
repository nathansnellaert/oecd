from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ECH@EXT_TEMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_extreme_temperature_exposure")
        print(f"Uploaded {data.num_rows} rows to extreme_temperature_exposure")
        
    save_state("extreme_temperature_exposure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
