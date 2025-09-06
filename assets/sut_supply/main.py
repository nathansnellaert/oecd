from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_SUPPLY_T1500")
    
    if data.num_rows > 0:
        upload_data(data, "sut_supply")
        print(f"Uploaded {data.num_rows} rows to sut_supply")
        
    save_state("sut_supply", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
