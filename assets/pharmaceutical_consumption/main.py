from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("HEALTH_PHMC@DF_PHMC_CONSUM")
    
    if data.num_rows > 0:
        upload_data(data, "pharmaceutical_consumption")
        print(f"Uploaded {data.num_rows} rows to pharmaceutical_consumption")
        
    save_state("pharmaceutical_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
