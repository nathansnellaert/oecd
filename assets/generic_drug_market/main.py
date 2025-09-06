from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("HEALTH_PHMC@DF_GEN_MRKT")
    
    if data.num_rows > 0:
        upload_data(data, "generic_drug_market")
        print(f"Uploaded {data.num_rows} rows to generic_drug_market")
        
    save_state("generic_drug_market", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
