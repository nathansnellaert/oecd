from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG_IV@DF_NAAG_IV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_naag_production")
        print(f"Uploaded {data.num_rows} rows to naag_production")
        
    save_state("naag_production", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
