from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ENE@DF_ENE")
    
    if data.num_rows > 0:
        upload_data(data, "energy_regions")
        print(f"Uploaded {data.num_rows} rows to energy_regions")
        
    save_state("energy_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
