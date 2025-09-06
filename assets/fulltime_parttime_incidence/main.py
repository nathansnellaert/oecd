from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FTPT@DF_FTPT_COMMON_INC")
    
    if data.num_rows > 0:
        upload_data(data, "fulltime_parttime_incidence")
        print(f"Uploaded {data.num_rows} rows to fulltime_parttime_incidence")
        
    save_state("fulltime_parttime_incidence", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
