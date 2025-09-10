from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_LVNG@DF_HEALTH_LVNG_BW")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_body_weight")
        print(f"Uploaded {data.num_rows} rows to body_weight")
        
    save_state("body_weight", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
