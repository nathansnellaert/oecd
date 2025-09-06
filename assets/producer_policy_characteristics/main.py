from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@DF_POL")
    
    if data.num_rows > 0:
        upload_data(data, "producer_policy_characteristics")
        print(f"Uploaded {data.num_rows} rows to producer_policy_characteristics")
        
    save_state("producer_policy_characteristics", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
