from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX_RECENT@DF_TAB33")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_africa_education_mismatch")
        print(f"Uploaded {data.num_rows} rows to africa_education_mismatch")
        
    save_state("africa_education_mismatch", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
