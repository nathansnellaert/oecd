from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REICO_FULL@DF_RDL")
    
    if data.num_rows > 0:
        upload_data(data, "reico_labour_market")
        print(f"Uploaded {data.num_rows} rows to reico_labour_market")
        
    save_state("reico_labour_market", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
