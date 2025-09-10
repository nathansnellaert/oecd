from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ERTR@DF_ERTR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_environmental_tax_revenue")
        print(f"Uploaded {data.num_rows} rows to environmental_tax_revenue")
        
    save_state("environmental_tax_revenue", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
