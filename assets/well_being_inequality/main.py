from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HSL@DF_HSL_CWB_INEQ")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_well_being_inequality")
        print(f"Uploaded {data.num_rows} rows to well_being_inequality")
        
    save_state("well_being_inequality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
