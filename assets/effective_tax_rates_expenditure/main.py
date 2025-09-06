from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ETR@DF_ETR_XBRD")
    
    if data.num_rows > 0:
        upload_data(data, "effective_tax_rates_expenditure")
        print(f"Uploaded {data.num_rows} rows to effective_tax_rates_expenditure")
        
    save_state("effective_tax_rates_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
