from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_IT@DF_EAG_IT_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "student_instruction_time_full")
        print(f"Uploaded {data.num_rows} rows to student_instruction_time_full")
        
    save_state("student_instruction_time_full", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
