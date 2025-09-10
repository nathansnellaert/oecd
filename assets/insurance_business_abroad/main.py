from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INS@DF_BUSINESS_ABROAD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_insurance_business_abroad")
        print(f"Uploaded {data.num_rows} rows to insurance_business_abroad")
        
    save_state("insurance_business_abroad", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
