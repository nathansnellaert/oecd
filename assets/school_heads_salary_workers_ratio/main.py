from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_SCH_REL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_school_heads_salary_workers_ratio")
        print(f"Uploaded {data.num_rows} rows to school_heads_salary_workers_ratio")
        
    save_state("school_heads_salary_workers_ratio", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
