from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_EDU@DF_EXCLU")
    
    if data.num_rows > 0:
        upload_data(data, "youth_education_exclusion")
        print(f"Uploaded {data.num_rows} rows to youth_education_exclusion")
        
    save_state("youth_education_exclusion", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
