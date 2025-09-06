from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_EAG_SAL_STA_TCH")
    
    if data.num_rows > 0:
        upload_data(data, "teachers_statutory_salary")
        print(f"Uploaded {data.num_rows} rows to teachers_statutory_salary")
        
    save_state("teachers_statutory_salary", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
