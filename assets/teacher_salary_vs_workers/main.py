from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_ACT@DF_TCH_REL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_teacher_salary_vs_workers")
        print(f"Uploaded {data.num_rows} rows to teacher_salary_vs_workers")
        
    save_state("teacher_salary_vs_workers", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
