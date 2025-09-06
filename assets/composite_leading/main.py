from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STES@DF_CLI")
    
    if data.num_rows > 0:
        upload_data(data, "composite_leading")
        print(f"Uploaded {data.num_rows} rows to composite_leading")
        
    save_state("composite_leading", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
