from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EARNINGS@DATASET")
    
    if data.num_rows > 0:
        upload_data(data, "earnings_full")
        print(f"Uploaded {data.num_rows} rows to earnings_full")
        
    save_state("earnings_full", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
