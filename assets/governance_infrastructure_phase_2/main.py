from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_INFRA_PH_2@DF_GOV_INFRA_PH_2")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_governance_infrastructure_phase_2")
        print(f"Uploaded {data.num_rows} rows to governance_infrastructure_phase_2")
        
    save_state("governance_infrastructure_phase_2", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
