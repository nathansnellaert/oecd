from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INS@DF_UNDERWRITING")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_insurance_premiums_claims_expenses")
        print(f"Uploaded {data.num_rows} rows to insurance_premiums_claims_expenses")
        
    save_state("insurance_premiums_claims_expenses", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
