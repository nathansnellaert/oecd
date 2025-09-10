from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SOE@DF_SOE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sustainable_ocean_economy")
        print(f"Uploaded {data.num_rows} rows to sustainable_ocean_economy")
        
    save_state("sustainable_ocean_economy", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
