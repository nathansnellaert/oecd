from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_IMMUN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_immunisations")
        print(f"Uploaded {data.num_rows} rows to immunisations")
        
    save_state("immunisations", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
