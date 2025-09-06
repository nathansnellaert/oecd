from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_WT@DF_EAG_WT_STA_TCH")
    
    if data.num_rows > 0:
        upload_data(data, "teachers_statutory_teaching_working_time")
        print(f"Uploaded {data.num_rows} rows to teachers_statutory_teaching_working_time")
        
    save_state("teachers_statutory_teaching_working_time", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
