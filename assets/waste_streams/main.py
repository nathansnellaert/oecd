from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WSTREAMS@DF_WSTREAMS")
    
    if data.num_rows > 0:
        upload_data(data, "waste_streams")
        print(f"Uploaded {data.num_rows} rows to waste_streams")
        
    save_state("waste_streams", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
