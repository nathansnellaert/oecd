from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_HHTYPE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_household_income_quintiles_by_type")
        print(f"Uploaded {data.num_rows} rows to household_income_quintiles_by_type")
        
    save_state("household_income_quintiles_by_type", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
