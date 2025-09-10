from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_EARN_REL_MALE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_earnings_differences_by_gender")
        print(f"Uploaded {data.num_rows} rows to earnings_differences_by_gender")
        
    save_state("earnings_differences_by_gender", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
