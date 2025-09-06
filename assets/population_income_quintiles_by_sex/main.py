from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_GENDER")
    
    if data.num_rows > 0:
        upload_data(data, "population_income_quintiles_by_sex")
        print(f"Uploaded {data.num_rows} rows to population_income_quintiles_by_sex")
        
    save_state("population_income_quintiles_by_sex", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
