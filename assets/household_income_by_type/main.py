from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_INC_HHT@DF_INC_HHT")
    
    if data.num_rows > 0:
        upload_data(data, "household_income_by_type")
        print(f"Uploaded {data.num_rows} rows to household_income_by_type")
        
    save_state("household_income_by_type", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
