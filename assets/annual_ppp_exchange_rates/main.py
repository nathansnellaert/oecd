from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE4")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_annual_ppp_exchange_rates")
        print(f"Uploaded {data.num_rows} rows to annual_ppp_exchange_rates")
        
    save_state("annual_ppp_exchange_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
