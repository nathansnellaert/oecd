from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BIMTS@DF_BIMTS_CPA_2_1")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_balanced_merchandise_trade_cpa")
        print(f"Uploaded {data.num_rows} rows to balanced_merchandise_trade_cpa")
        
    save_state("balanced_merchandise_trade_cpa", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
