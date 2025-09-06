from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STES@DF_CSBAR")
    
    if data.num_rows > 0:
        upload_data(data, "consumer_barometer")
        print(f"Uploaded {data.num_rows} rows to consumer_barometer")
        
    save_state("consumer_barometer", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
