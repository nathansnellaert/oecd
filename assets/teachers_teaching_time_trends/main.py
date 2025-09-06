from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_WT_TREND@DF_EAG_WT_TREND")
    
    if data.num_rows > 0:
        upload_data(data, "teachers_teaching_time_trends")
        print(f"Uploaded {data.num_rows} rows to teachers_teaching_time_trends")
        
    save_state("teachers_teaching_time_trends", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
