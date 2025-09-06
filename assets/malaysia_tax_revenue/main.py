from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_ASAP@DF_REVMYS")
    
    if data.num_rows > 0:
        upload_data(data, "malaysia_tax_revenue")
        print(f"Uploaded {data.num_rows} rows to malaysia_tax_revenue")
        
    save_state("malaysia_tax_revenue", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
