from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_LF")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_labour_force_participation")
        print(f"Uploaded {data.num_rows} rows to labour_force_participation")
        
    save_state("labour_force_participation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
