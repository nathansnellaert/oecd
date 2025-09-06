from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_WT@DF_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "teaching_working_time_full")
        print(f"Uploaded {data.num_rows} rows to teaching_working_time_full")
        
    save_state("teaching_working_time_full", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
