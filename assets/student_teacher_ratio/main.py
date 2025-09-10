from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_STR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_student_teacher_ratio")
        print(f"Uploaded {data.num_rows} rows to student_teacher_ratio")
        
    save_state("student_teacher_ratio", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
