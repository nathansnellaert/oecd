from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_AFRICA@DF_REVMRT")
    
    if data.num_rows > 0:
        upload_data(data, "mauritania_tax_revenue")
        print(f"Uploaded {data.num_rows} rows to mauritania_tax_revenue")
        
    save_state("mauritania_tax_revenue", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
