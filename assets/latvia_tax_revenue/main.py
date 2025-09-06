from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_OECD@DF_REVLVA")
    
    if data.num_rows > 0:
        upload_data(data, "latvia_tax_revenue")
        print(f"Uploaded {data.num_rows} rows to latvia_tax_revenue")
        
    save_state("latvia_tax_revenue", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
