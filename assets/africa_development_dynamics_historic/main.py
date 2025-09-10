from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_HISTORIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_africa_development_dynamics_historic")
        print(f"Uploaded {data.num_rows} rows to africa_development_dynamics_historic")
        
    save_state("africa_development_dynamics_historic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
