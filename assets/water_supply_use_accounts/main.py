from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_PSUT@DF_WATER_PSUT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_water_supply_use_accounts")
        print(f"Uploaded {data.num_rows} rows to water_supply_use_accounts")
        
    save_state("water_supply_use_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
