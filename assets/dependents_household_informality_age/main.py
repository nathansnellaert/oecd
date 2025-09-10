from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B19")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_dependents_household_informality_age")
        print(f"Uploaded {data.num_rows} rows to dependents_household_informality_age")
        
    save_state("dependents_household_informality_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
