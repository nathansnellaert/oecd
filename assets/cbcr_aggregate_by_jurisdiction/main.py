from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CBCR@DF_CBCRI")
    
    if data.num_rows > 0:
        upload_data(data, "cbcr_aggregate_by_jurisdiction")
        print(f"Uploaded {data.num_rows} rows to cbcr_aggregate_by_jurisdiction")
        
    save_state("cbcr_aggregate_by_jurisdiction", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
