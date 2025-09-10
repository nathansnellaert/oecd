from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_INC_INC@DF_INC_INC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_household_income_by_quintile")
        print(f"Uploaded {data.num_rows} rows to household_income_by_quintile")
        
    save_state("household_income_by_quintile", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
