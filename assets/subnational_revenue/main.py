from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DASHBOARD@REV")
    
    if data.num_rows > 0:
        upload_data(data, "subnational_revenue")
        print(f"Uploaded {data.num_rows} rows to subnational_revenue")
        
    save_state("subnational_revenue", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
