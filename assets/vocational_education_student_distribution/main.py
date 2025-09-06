from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_DIST_VET")
    
    if data.num_rows > 0:
        upload_data(data, "vocational_education_student_distribution")
        print(f"Uploaded {data.num_rows} rows to vocational_education_student_distribution")
        
    save_state("vocational_education_student_distribution", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
