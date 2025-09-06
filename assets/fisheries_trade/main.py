from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FISH_TRADE@DF_FISH_TRADE")
    
    if data.num_rows > 0:
        upload_data(data, "fisheries_trade")
        print(f"Uploaded {data.num_rows} rows to fisheries_trade")
        
    save_state("fisheries_trade", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
