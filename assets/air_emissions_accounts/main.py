from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AEA@DF_AEA")
    
    if data.num_rows > 0:
        upload_data(data, "air_emissions_accounts")
        print(f"Uploaded {data.num_rows} rows to air_emissions_accounts")
        
    save_state("air_emissions_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
