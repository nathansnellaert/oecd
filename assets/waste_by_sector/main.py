from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WSECTOR@DF_WSECTOR")
    
    if data.num_rows > 0:
        upload_data(data, "waste_by_sector")
        print(f"Uploaded {data.num_rows} rows to waste_by_sector")
        
    save_state("waste_by_sector", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
