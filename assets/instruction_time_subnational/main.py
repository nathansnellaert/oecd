from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_IT@DF_EAG_IT_ISCED_REG")
    
    if data.num_rows > 0:
        upload_data(data, "instruction_time_subnational")
        print(f"Uploaded {data.num_rows} rows to instruction_time_subnational")
        
    save_state("instruction_time_subnational", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
