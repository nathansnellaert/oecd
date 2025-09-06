from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_PTR@DF_PTRSA")
    
    if data.num_rows > 0:
        upload_data(data, "tax_rates_work_minimum_income")
        print(f"Uploaded {data.num_rows} rows to tax_rates_work_minimum_income")
        
    save_state("tax_rates_work_minimum_income", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
