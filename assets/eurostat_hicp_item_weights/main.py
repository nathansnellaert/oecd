from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PRICES@DF_PRICES_HICP_IT_W")
    
    if data.num_rows > 0:
        upload_data(data, "eurostat_hicp_item_weights")
        print(f"Uploaded {data.num_rows} rows to eurostat_hicp_item_weights")
        
    save_state("eurostat_hicp_item_weights", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
