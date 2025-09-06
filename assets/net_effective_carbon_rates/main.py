from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NECR@DF_NECRS")
    
    if data.num_rows > 0:
        upload_data(data, "net_effective_carbon_rates")
        print(f"Uploaded {data.num_rows} rows to net_effective_carbon_rates")
        
    save_state("net_effective_carbon_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
