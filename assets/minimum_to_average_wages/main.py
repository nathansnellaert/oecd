from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EARNINGS@MIN2AVE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_minimum_to_average_wages")
        print(f"Uploaded {data.num_rows} rows to minimum_to_average_wages")
        
    save_state("minimum_to_average_wages", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
