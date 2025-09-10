from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_ABSTRACT@DF_WATER_ABSTRACT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_freshwater_abstractions")
        print(f"Uploaded {data.num_rows} rows to freshwater_abstractions")
        
    save_state("freshwater_abstractions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
