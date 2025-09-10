from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EPS@DF_EPS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_environmental_policy_stringency_index")
        print(f"Uploaded {data.num_rows} rows to environmental_policy_stringency_index")
        
    save_state("environmental_policy_stringency_index", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
