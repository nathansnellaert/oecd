from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE13_BAL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sector_balancing_items")
        print(f"Uploaded {data.num_rows} rows to sector_balancing_items")
        
    save_state("sector_balancing_items", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
