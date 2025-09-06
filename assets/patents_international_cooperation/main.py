from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PATENTS@DF_PATENTS_INDICATORS")
    
    if data.num_rows > 0:
        upload_data(data, "patents_international_cooperation")
        print(f"Uploaded {data.num_rows} rows to patents_international_cooperation")
        
    save_state("patents_international_cooperation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
