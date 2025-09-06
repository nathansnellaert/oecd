from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_MULTI@DF_MULTI")
    
    if data.num_rows > 0:
        upload_data(data, "multilateral_system_use")
        print(f"Uploaded {data.num_rows} rows to multilateral_system_use")
        
    save_state("multilateral_system_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
