from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NECR@DF_NECRSHARES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_emissions_priced_shares")
        print(f"Uploaded {data.num_rows} rows to emissions_priced_shares")
        
    save_state("emissions_priced_shares", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
