from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ENE@DF_ENE_CONSUMPTION")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_energy_consumption_regions")
        print(f"Uploaded {data.num_rows} rows to energy_consumption_regions")
        
    save_state("energy_consumption_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
