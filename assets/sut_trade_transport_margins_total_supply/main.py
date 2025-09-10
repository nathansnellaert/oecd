from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_INDICATOR_OTTM_TS_O")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sut_trade_transport_margins_total_supply")
        print(f"Uploaded {data.num_rows} rows to sut_trade_transport_margins_total_supply")
        
    save_state("sut_trade_transport_margins_total_supply", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
