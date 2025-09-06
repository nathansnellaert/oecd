from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INVPT_EMP@DF_INVPT_D")
    
    if data.num_rows > 0:
        upload_data(data, "involuntary_part_time_employment")
        print(f"Uploaded {data.num_rows} rows to involuntary_part_time_employment")
        
    save_state("involuntary_part_time_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
