from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_RAW_ADULT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_adult_students_by_age")
        print(f"Uploaded {data.num_rows} rows to adult_students_by_age")
        
    save_state("adult_students_by_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
