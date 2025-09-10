from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_TCH_COM")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_teachers_salary_comparative")
        print(f"Uploaded {data.num_rows} rows to teachers_salary_comparative")
        
    save_state("teachers_salary_comparative", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
