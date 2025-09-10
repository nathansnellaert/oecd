from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B7")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_population_household_informality_welfare_quintile")
        print(f"Uploaded {data.num_rows} rows to population_household_informality_welfare_quintile")
        
    save_state("population_household_informality_welfare_quintile", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
