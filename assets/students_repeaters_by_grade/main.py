from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_RAW_RPTR")
    
    if data.num_rows > 0:
        upload_data(data, "students_repeaters_by_grade")
        print(f"Uploaded {data.num_rows} rows to students_repeaters_by_grade")
        
    save_state("students_repeaters_by_grade", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
