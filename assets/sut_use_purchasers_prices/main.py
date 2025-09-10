from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_USEPP_T1600")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sut_use_purchasers_prices")
        print(f"Uploaded {data.num_rows} rows to sut_use_purchasers_prices")
        
    save_state("sut_use_purchasers_prices", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
