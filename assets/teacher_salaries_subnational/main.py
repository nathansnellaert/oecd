from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_TCH_REG")
    
    if data.num_rows > 0:
        upload_data(data, "teacher_salaries_subnational")
        print(f"Uploaded {data.num_rows} rows to teacher_salaries_subnational")
        
    save_state("teacher_salaries_subnational", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
