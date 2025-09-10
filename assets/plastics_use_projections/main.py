from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PU_P@DF_PU_P")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_plastics_use_projections")
        print(f"Uploaded {data.num_rows} rows to plastics_use_projections")
        
    save_state("plastics_use_projections", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
