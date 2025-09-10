from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_DEMO@DF_MOBILITY")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_internal_mobility")
        print(f"Uploaded {data.num_rows} rows to regional_internal_mobility")
        
    save_state("regional_internal_mobility", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
