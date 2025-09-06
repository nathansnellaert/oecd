from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PATENTS@DF_PATENTS_DOMESTIC")
    
    if data.num_rows > 0:
        upload_data(data, "patents_domestic_ownership_abroad")
        print(f"Uploaded {data.num_rows} rows to patents_domestic_ownership_abroad")
        
    save_state("patents_domestic_ownership_abroad", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
