from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10_IDC@DF_TABLE5_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "annual_household_consumption_expenditure")
        print(f"Uploaded {data.num_rows} rows to annual_household_consumption_expenditure")
        
    save_state("annual_household_consumption_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
