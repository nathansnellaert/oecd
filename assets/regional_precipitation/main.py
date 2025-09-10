from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_CLIM@DF_PRECIPITATION")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_precipitation")
        print(f"Uploaded {data.num_rows} rows to regional_precipitation")
        
    save_state("regional_precipitation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
