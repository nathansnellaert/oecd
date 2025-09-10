from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_INC_MSI@DF_INC_MSI")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_household_income_by_source")
        print(f"Uploaded {data.num_rows} rows to household_income_by_source")
        
    save_state("household_income_by_source", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
