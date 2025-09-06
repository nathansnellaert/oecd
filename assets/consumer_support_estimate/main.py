from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@DF_CSE")
    
    if data.num_rows > 0:
        upload_data(data, "consumer_support_estimate")
        print(f"Uploaded {data.num_rows} rows to consumer_support_estimate")
        
    save_state("consumer_support_estimate", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
