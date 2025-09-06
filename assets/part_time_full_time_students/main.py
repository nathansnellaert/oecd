from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_SHARE_PT_FT")
    
    if data.num_rows > 0:
        upload_data(data, "part_time_full_time_students")
        print(f"Uploaded {data.num_rows} rows to part_time_full_time_students")
        
    save_state("part_time_full_time_students", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
