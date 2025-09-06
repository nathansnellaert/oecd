from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CPU@DF_CPU")
    
    if data.num_rows > 0:
        upload_data(data, "climate_policy_uncertainty")
        print(f"Uploaded {data.num_rows} rows to climate_policy_uncertainty")
        
    save_state("climate_policy_uncertainty", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
