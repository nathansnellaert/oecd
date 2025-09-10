from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_TDG_SPS_GPC@DF_GOV_TDG_SPS_GPC_2023")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_trust_satisfaction_public_services")
        print(f"Uploaded {data.num_rows} rows to trust_satisfaction_public_services")
        
    save_state("trust_satisfaction_public_services", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
