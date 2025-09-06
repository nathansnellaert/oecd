from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ECH@COAS_FLOOD")
    
    if data.num_rows > 0:
        upload_data(data, "coastal_flood_exposure")
        print(f"Uploaded {data.num_rows} rows to coastal_flood_exposure")
        
    save_state("coastal_flood_exposure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
