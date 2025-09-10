from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_EAG_SAL_STA_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_teacher_school_head_statutory_salaries")
        print(f"Uploaded {data.num_rows} rows to teacher_school_head_statutory_salaries")
        
    save_state("teacher_school_head_statutory_salaries", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
