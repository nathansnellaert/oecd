from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAT_RES@DF_NAT_RES")
    
    if data.num_rows > 0:
        upload_data(data, "mineral_energy_resources")
        print(f"Uploaded {data.num_rows} rows to mineral_energy_resources")
        
    save_state("mineral_energy_resources", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
