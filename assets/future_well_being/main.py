from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HSL@DF_HSL_FWB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_future_well_being")
        print(f"Uploaded {data.num_rows} rows to future_well_being")
        
    save_state("future_well_being", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
