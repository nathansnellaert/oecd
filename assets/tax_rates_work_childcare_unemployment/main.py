from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_PTR@DF_PTRCCUB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_tax_rates_work_childcare_unemployment")
        print(f"Uploaded {data.num_rows} rows to tax_rates_work_childcare_unemployment")
        
    save_state("tax_rates_work_childcare_unemployment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
