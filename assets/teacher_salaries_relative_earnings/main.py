from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_TCH_REL")
    
    if data.num_rows > 0:
        upload_data(data, "teacher_salaries_relative_earnings")
        print(f"Uploaded {data.num_rows} rows to teacher_salaries_relative_earnings")
        
    save_state("teacher_salaries_relative_earnings", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
