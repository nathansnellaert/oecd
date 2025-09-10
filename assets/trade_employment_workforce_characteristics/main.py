from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIMBC_2023@DF_TIMBC_2023")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_trade_employment_workforce_characteristics")
        print(f"Uploaded {data.num_rows} rows to trade_employment_workforce_characteristics")
        
    save_state("trade_employment_workforce_characteristics", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
