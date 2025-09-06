from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@DF_MONEVA")
    
    if data.num_rows > 0:
        upload_data(data, "agricultural_policy_monitoring_evaluation")
        print(f"Uploaded {data.num_rows} rows to agricultural_policy_monitoring_evaluation")
        
    save_state("agricultural_policy_monitoring_evaluation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
