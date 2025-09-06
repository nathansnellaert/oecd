from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_TRANS_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "youth_education_work_transition")
        print(f"Uploaded {data.num_rows} rows to youth_education_work_transition")
        
    save_state("youth_education_work_transition", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
