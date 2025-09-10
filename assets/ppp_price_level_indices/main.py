from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PPP@DF_PPP_CPL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ppp_price_level_indices")
        print(f"Uploaded {data.num_rows} rows to ppp_price_level_indices")
        
    save_state("ppp_price_level_indices", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
