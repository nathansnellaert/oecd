from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX_RECENT@DF_TAB35")
    
    if data.num_rows > 0:
        upload_data(data, "africa_employment_by_occupation")
        print(f"Uploaded {data.num_rows} rows to africa_employment_by_occupation")
        
    save_state("africa_employment_by_occupation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
