from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG@DF_NAAG_III_CG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_aggregate_demand_components")
        print(f"Uploaded {data.num_rows} rows to aggregate_demand_components")
        
    save_state("aggregate_demand_components", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
