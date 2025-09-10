from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_SURG_PROC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_surgical_procedures")
        print(f"Uploaded {data.num_rows} rows to surgical_procedures")
        
    save_state("surgical_procedures", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
