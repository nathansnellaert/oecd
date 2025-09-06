from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_VALUATION_T1634")
    
    if data.num_rows > 0:
        upload_data(data, "sut_product_subsidies")
        print(f"Uploaded {data.num_rows} rows to sut_product_subsidies")
        
    save_state("sut_product_subsidies", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
