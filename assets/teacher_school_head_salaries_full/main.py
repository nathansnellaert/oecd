from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_ACT@DF_EAG_SAL_ACT_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "teacher_school_head_salaries_full")
        print(f"Uploaded {data.num_rows} rows to teacher_school_head_salaries_full")
        
    save_state("teacher_school_head_salaries_full", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
