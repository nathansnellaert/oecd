from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_USEBP_T1612")
    
    if data.num_rows > 0:
        upload_data(data, "sut_import_use_basic_prices")
        print(f"Uploaded {data.num_rows} rows to sut_import_use_basic_prices")
        
    save_state("sut_import_use_basic_prices", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
