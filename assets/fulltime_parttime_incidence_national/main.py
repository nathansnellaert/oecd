from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FTPT@DF_FTPT_NATIONAL_INC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_fulltime_parttime_incidence_national")
        print(f"Uploaded {data.num_rows} rows to fulltime_parttime_incidence_national")
        
    save_state("fulltime_parttime_incidence_national", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
