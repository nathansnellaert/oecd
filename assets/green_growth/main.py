from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GG@DF_GREEN_GROWTH")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_green_growth")
        print(f"Uploaded {data.num_rows} rows to green_growth")
        
    save_state("green_growth", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
