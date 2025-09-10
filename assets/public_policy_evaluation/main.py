from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_PE@DF_GOV_PE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_public_policy_evaluation")
        print(f"Uploaded {data.num_rows} rows to public_policy_evaluation")
        
    save_state("public_policy_evaluation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
