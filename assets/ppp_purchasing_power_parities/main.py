from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PPP@DF_PPP_PPP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ppp_purchasing_power_parities")
        print(f"Uploaded {data.num_rows} rows to ppp_purchasing_power_parities")
        
    save_state("ppp_purchasing_power_parities", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
