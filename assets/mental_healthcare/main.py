from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_MH")
    
    if data.num_rows > 0:
        upload_data(data, "mental_healthcare")
        print(f"Uploaded {data.num_rows} rows to mental_healthcare")
        
    save_state("mental_healthcare", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
