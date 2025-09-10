from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_ENRL_RATE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_enrolment_rate_by_age")
        print(f"Uploaded {data.num_rows} rows to enrolment_rate_by_age")
        
    save_state("enrolment_rate_by_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
