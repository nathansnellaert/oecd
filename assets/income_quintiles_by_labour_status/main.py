from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_LABOUR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_income_quintiles_by_labour_status")
        print(f"Uploaded {data.num_rows} rows to income_quintiles_by_labour_status")
        
    save_state("income_quintiles_by_labour_status", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
