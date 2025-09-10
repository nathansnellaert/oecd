from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE2")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_national_income_saving_lending")
        print(f"Uploaded {data.num_rows} rows to national_income_saving_lending")
        
    save_state("national_income_saving_lending", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
