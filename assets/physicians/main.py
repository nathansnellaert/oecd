from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_EMP_REAC@DF_PHYS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_physicians")
        print(f"Uploaded {data.num_rows} rows to physicians")
        
    save_state("physicians", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
