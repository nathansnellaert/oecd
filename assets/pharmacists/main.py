from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_REAC_EMP@DF_PHST")
    
    if data.num_rows > 0:
        upload_data(data, "pharmacists")
        print(f"Uploaded {data.num_rows} rows to pharmacists")
        
    save_state("pharmacists", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
