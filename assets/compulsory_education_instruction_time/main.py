from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_IT@DF_EAG_IT_ISCED")
    
    if data.num_rows > 0:
        upload_data(data, "compulsory_education_instruction_time")
        print(f"Uploaded {data.num_rows} rows to compulsory_education_instruction_time")
        
    save_state("compulsory_education_instruction_time", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
