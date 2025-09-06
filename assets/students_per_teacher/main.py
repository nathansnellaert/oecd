from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_PERS@DF_UOE_NF_PERS_STU")
    
    if data.num_rows > 0:
        upload_data(data, "students_per_teacher")
        print(f"Uploaded {data.num_rows} rows to students_per_teacher")
        
    save_state("students_per_teacher", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
