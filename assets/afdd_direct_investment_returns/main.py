from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_TAB22")
    
    if data.num_rows > 0:
        upload_data(data, "afdd_direct_investment_returns")
        print(f"Uploaded {data.num_rows} rows to afdd_direct_investment_returns")
        
    save_state("afdd_direct_investment_returns", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
