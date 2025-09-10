from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_INDICATOR_P7_P3S14_B")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sut_imported_products_household_consumption")
        print(f"Uploaded {data.num_rows} rows to sut_imported_products_household_consumption")
        
    save_state("sut_imported_products_household_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
