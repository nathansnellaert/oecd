from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INS@DF_NB_COMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_insurance_companies_employees")
        print(f"Uploaded {data.num_rows} rows to insurance_companies_employees")
        
    save_state("insurance_companies_employees", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
