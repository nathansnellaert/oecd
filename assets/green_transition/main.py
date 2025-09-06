from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GREEN_TRANSITION@DF_GREEN_TRANSITION")
    
    if data.num_rows > 0:
        upload_data(data, "green_transition")
        print(f"Uploaded {data.num_rows} rows to green_transition")
        
    save_state("green_transition", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
