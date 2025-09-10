from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_EARN_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_education_earnings_full")
        print(f"Uploaded {data.num_rows} rows to education_earnings_full")
        
    save_state("education_earnings_full", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
