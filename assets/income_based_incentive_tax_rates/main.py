from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ETR@DF_ETR_IBRD")
    
    if data.num_rows > 0:
        upload_data(data, "income_based_incentive_tax_rates")
        print(f"Uploaded {data.num_rows} rows to income_based_incentive_tax_rates")
        
    save_state("income_based_incentive_tax_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
