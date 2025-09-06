from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_TREND@DF_EAG_SAL_TREND_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "teacher_salary_trends_complete")
        print(f"Uploaded {data.num_rows} rows to teacher_salary_trends_complete")
        
    save_state("teacher_salary_trends_complete", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
