from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FISH_FLEET@DF_FISH_FLEET")
    
    if data.num_rows > 0:
        upload_data(data, "fishing_fleet")
        print(f"Uploaded {data.num_rows} rows to fishing_fleet")
        
    save_state("fishing_fleet", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
