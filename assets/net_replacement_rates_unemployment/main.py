from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_NRR@DF_NRR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_net_replacement_rates_unemployment")
        print(f"Uploaded {data.num_rows} rows to net_replacement_rates_unemployment")
        
    save_state("net_replacement_rates_unemployment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
