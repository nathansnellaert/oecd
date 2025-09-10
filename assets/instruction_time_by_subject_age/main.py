from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_IT@DF_EAG_IT_SUBJ_AGE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_instruction_time_by_subject_age")
        print(f"Uploaded {data.num_rows} rows to instruction_time_by_subject_age")
        
    save_state("instruction_time_by_subject_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
