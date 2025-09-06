from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE4_PPP_P31S14")
    
    if data.num_rows > 0:
        upload_data(data, "ppp_household_consumption")
        print(f"Uploaded {data.num_rows} rows to ppp_household_consumption")
        
    save_state("ppp_household_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
