from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("HEALTH_PHMC@DF_PHMC_SALES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_pharmaceutical_sales")
        print(f"Uploaded {data.num_rows} rows to pharmaceutical_sales")
        
    save_state("pharmaceutical_sales", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
