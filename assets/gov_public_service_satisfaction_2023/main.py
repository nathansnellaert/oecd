from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_TDG_SPS_GPC@DF_GOV_SPS_2023")
    
    if data.num_rows > 0:
        upload_data(data, "gov_public_service_satisfaction_2023")
        print(f"Uploaded {data.num_rows} rows to gov_public_service_satisfaction_2023")
        
    save_state("gov_public_service_satisfaction_2023", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
