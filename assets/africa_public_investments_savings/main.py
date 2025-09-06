from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX_RECENT@DF_TAB24")
    
    if data.num_rows > 0:
        upload_data(data, "africa_public_investments_savings")
        print(f"Uploaded {data.num_rows} rows to africa_public_investments_savings")
        
    save_state("africa_public_investments_savings", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
