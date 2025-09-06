from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_HHOWN")
    
    if data.num_rows > 0:
        upload_data(data, "household_income_quintiles_by_ownership")
        print(f"Uploaded {data.num_rows} rows to household_income_quintiles_by_ownership")
        
    save_state("household_income_quintiles_by_ownership", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
