from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EARNINGS@RMW")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_real_minimum_wages")
        print(f"Uploaded {data.num_rows} rows to real_minimum_wages")
        
    save_state("real_minimum_wages", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
