from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PEFA@DF_PEFAUSE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_energy_flow_use_activity")
        print(f"Uploaded {data.num_rows} rows to energy_flow_use_activity")
        
    save_state("energy_flow_use_activity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
