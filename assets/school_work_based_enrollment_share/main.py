from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_SHARE_VET")
    
    if data.num_rows > 0:
        upload_data(data, "school_work_based_enrollment_share")
        print(f"Uploaded {data.num_rows} rows to school_work_based_enrollment_share")
        
    save_state("school_work_based_enrollment_share", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
