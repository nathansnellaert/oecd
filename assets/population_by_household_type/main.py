from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_HHGROUP")
    
    if data.num_rows > 0:
        upload_data(data, "population_by_household_type")
        print(f"Uploaded {data.num_rows} rows to population_by_household_type")
        
    save_state("population_by_household_type", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
