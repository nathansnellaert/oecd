from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B18")
    
    if data.num_rows > 0:
        upload_data(data, "hourly_earnings_formal_informal_ratio")
        print(f"Uploaded {data.num_rows} rows to hourly_earnings_formal_informal_ratio")
        
    save_state("hourly_earnings_formal_informal_ratio", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
