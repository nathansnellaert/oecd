from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B17")
    
    if data.num_rows > 0:
        upload_data(data, "health_expenditure_household_informality")
        print(f"Uploaded {data.num_rows} rows to health_expenditure_household_informality")
        
    save_state("health_expenditure_household_informality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
