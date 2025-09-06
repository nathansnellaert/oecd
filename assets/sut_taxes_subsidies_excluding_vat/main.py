from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_VALUATION_T1631")
    
    if data.num_rows > 0:
        upload_data(data, "sut_taxes_subsidies_excluding_vat")
        print(f"Uploaded {data.num_rows} rows to sut_taxes_subsidies_excluding_vat")
        
    save_state("sut_taxes_subsidies_excluding_vat", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
