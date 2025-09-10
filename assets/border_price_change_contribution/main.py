from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@DF_BOR_PRI")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_border_price_change_contribution")
        print(f"Uploaded {data.num_rows} rows to border_price_change_contribution")
        
    save_state("border_price_change_contribution", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
