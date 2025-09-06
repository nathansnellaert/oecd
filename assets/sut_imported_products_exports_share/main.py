from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_INDICATOR_P7_P6_B")
    
    if data.num_rows > 0:
        upload_data(data, "sut_imported_products_exports_share")
        print(f"Uploaded {data.num_rows} rows to sut_imported_products_exports_share")
        
    save_state("sut_imported_products_exports_share", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
