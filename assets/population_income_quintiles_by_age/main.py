from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_AGE")
    
    if data.num_rows > 0:
        upload_data(data, "population_income_quintiles_by_age")
        print(f"Uploaded {data.num_rows} rows to population_income_quintiles_by_age")
        
    save_state("population_income_quintiles_by_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
