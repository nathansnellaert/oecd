from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_LVNG@DF_HEALTH_LVNG_VP")
    
    if data.num_rows > 0:
        upload_data(data, "vaping_product_use")
        print(f"Uploaded {data.num_rows} rows to vaping_product_use")
        
    save_state("vaping_product_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
