from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TEC_ISIC4@DF_TEC03")
    
    if data.num_rows > 0:
        upload_data(data, "trade_by_partner_zones")
        print(f"Uploaded {data.num_rows} rows to trade_by_partner_zones")
        
    save_state("trade_by_partner_zones", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
