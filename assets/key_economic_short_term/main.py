from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KEI@DF_KEI")
    
    if data.num_rows > 0:
        upload_data(data, "key_economic_short_term")
        print(f"Uploaded {data.num_rows} rows to key_economic_short_term")
        
    save_state("key_economic_short_term", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
