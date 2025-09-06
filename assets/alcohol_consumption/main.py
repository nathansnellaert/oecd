from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_LVNG@DF_HEALTH_LVNG_AC")
    
    if data.num_rows > 0:
        upload_data(data, "alcohol_consumption")
        print(f"Uploaded {data.num_rows} rows to alcohol_consumption")
        
    save_state("alcohol_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
