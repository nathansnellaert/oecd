from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_VALUATION_T1633")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sut_taxes_on_products")
        print(f"Uploaded {data.num_rows} rows to sut_taxes_on_products")
        
    save_state("sut_taxes_on_products", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
