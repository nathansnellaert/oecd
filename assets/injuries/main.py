from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_I")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_injuries")
        print(f"Uploaded {data.num_rows} rows to injuries")
        
    save_state("injuries", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
