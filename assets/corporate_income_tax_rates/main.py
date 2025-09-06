from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_CIT@DF_CIT")
    
    if data.num_rows > 0:
        upload_data(data, "corporate_income_tax_rates")
        print(f"Uploaded {data.num_rows} rows to corporate_income_tax_rates")
        
    save_state("corporate_income_tax_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
