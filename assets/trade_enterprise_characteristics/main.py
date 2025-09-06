from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TEC_ISIC4@DF_TEC")
    
    if data.num_rows > 0:
        upload_data(data, "trade_enterprise_characteristics")
        print(f"Uploaded {data.num_rows} rows to trade_enterprise_characteristics")
        
    save_state("trade_enterprise_characteristics", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
