from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PEFA_BR@DF_PEFABR")
    
    if data.num_rows > 0:
        upload_data(data, "energy_flow_accounts_bridging")
        print(f"Uploaded {data.num_rows} rows to energy_flow_accounts_bridging")
        
    save_state("energy_flow_accounts_bridging", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
