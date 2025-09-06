from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_COMPASS_KEY@DF_COMPASS_KEY")
    
    if data.num_rows > 0:
        upload_data(data, "compass_key_indicators")
        print(f"Uploaded {data.num_rows} rows to compass_key_indicators")
        
    save_state("compass_key_indicators", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
