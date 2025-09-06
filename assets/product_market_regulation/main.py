from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PMR@DF_PMR")
    
    if data.num_rows > 0:
        upload_data(data, "product_market_regulation")
        print(f"Uploaded {data.num_rows} rows to product_market_regulation")
        
    save_state("product_market_regulation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
