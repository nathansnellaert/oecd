from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_TCH")
    
    if data.num_rows > 0:
        upload_data(data, "teachers_salaries")
        print(f"Uploaded {data.num_rows} rows to teachers_salaries")
        
    save_state("teachers_salaries", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
