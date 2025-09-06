from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_INDICATOR_P2_PRODUCT_SHARE_B")
    
    if data.num_rows > 0:
        upload_data(data, "sut_intermediate_consumption_product_shares")
        print(f"Uploaded {data.num_rows} rows to sut_intermediate_consumption_product_shares")
        
    save_state("sut_intermediate_consumption_product_shares", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
