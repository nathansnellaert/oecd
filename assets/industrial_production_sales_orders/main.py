from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STES@DF_INDSERV")
    
    if data.num_rows > 0:
        upload_data(data, "industrial_production_sales_orders")
        print(f"Uploaded {data.num_rows} rows to industrial_production_sales_orders")
        
    save_state("industrial_production_sales_orders", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
