from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR@DF_OUTLOOK_2025_2034")
    
    if data.num_rows > 0:
        upload_data(data, "agricultural_outlook_2025_2034")
        print(f"Uploaded {data.num_rows} rows to agricultural_outlook_2025_2034")
        
    save_state("agricultural_outlook_2025_2034", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
