from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TEC_ISIC4@DF_TEC06")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_trade_by_trader_type")
        print(f"Uploaded {data.num_rows} rows to trade_by_trader_type")
        
    save_state("trade_by_trader_type", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
