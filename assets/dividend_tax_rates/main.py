from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_CIT@DF_CIT_DIVD_INCOME")
    
    if data.num_rows > 0:
        upload_data(data, "dividend_tax_rates")
        print(f"Uploaded {data.num_rows} rows to dividend_tax_rates")
        
    save_state("dividend_tax_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
