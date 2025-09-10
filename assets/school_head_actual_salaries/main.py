from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_ACT@DF_SCH")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_school_head_actual_salaries")
        print(f"Uploaded {data.num_rows} rows to school_head_actual_salaries")
        
    save_state("school_head_actual_salaries", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
