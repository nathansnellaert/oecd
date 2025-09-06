from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TENURE@DF_TENURE_AVE")
    
    if data.num_rows > 0:
        upload_data(data, "dsd_tenure@tenure_ave")
        print(f"Uploaded {data.num_rows} rows to dsd_tenure@tenure_ave")
        
    save_state("dsd_tenure@tenure_ave", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
