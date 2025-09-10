from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX_RECENT@DF_TAB31")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_africa_informal_economies_employment")
        print(f"Uploaded {data.num_rows} rows to africa_informal_economies_employment")
        
    save_state("africa_informal_economies_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
