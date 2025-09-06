from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B6")
    
    if data.num_rows > 0:
        upload_data(data, "population_urbanisation_household_informality")
        print(f"Uploaded {data.num_rows} rows to population_urbanisation_household_informality")
        
    save_state("population_urbanisation_household_informality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
