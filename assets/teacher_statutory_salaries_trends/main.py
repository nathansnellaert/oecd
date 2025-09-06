from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_TREND@DF_TCH_STA")
    
    if data.num_rows > 0:
        upload_data(data, "teacher_statutory_salaries_trends")
        print(f"Uploaded {data.num_rows} rows to teacher_statutory_salaries_trends")
        
    save_state("teacher_statutory_salaries_trends", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
