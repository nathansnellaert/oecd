from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INDUSTRIAL_POLICY@DF_GRANTAX")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quis_policy_grants_tax")
        print(f"Uploaded {data.num_rows} rows to quis_policy_grants_tax")
        
    save_state("quis_policy_grants_tax", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
