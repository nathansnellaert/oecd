from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDS_BERD@DF_BERD_SOF_SIZE")
    
    if data.num_rows > 0:
        upload_data(data, "business_rd_by_size_and_funding")
        print(f"Uploaded {data.num_rows} rows to business_rd_by_size_and_funding")
        
    save_state("business_rd_by_size_and_funding", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
