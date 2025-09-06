from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX_RECENT@DF_TAB09")
    
    if data.num_rows > 0:
        upload_data(data, "africa_inequality_poverty")
        print(f"Uploaded {data.num_rows} rows to africa_inequality_poverty")
        
    save_state("africa_inequality_poverty", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
