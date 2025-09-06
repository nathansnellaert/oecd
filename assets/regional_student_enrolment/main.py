from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_EDU@DF_ENROL")
    
    if data.num_rows > 0:
        upload_data(data, "regional_student_enrolment")
        print(f"Uploaded {data.num_rows} rows to regional_student_enrolment")
        
    save_state("regional_student_enrolment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
