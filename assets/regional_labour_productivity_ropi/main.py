from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ECO_ROPI@DF_LPR_ROPI")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_labour_productivity_ropi")
        print(f"Uploaded {data.num_rows} rows to regional_labour_productivity_ropi")
        
    save_state("regional_labour_productivity_ropi", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
