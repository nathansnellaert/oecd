from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_WT@DF_STA_TCH_REG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_teachers_teaching_time_subnational")
        print(f"Uploaded {data.num_rows} rows to teachers_teaching_time_subnational")
        
    save_state("teachers_teaching_time_subnational", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
