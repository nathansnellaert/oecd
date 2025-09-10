from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_DEMO_DDOWN@DF_POP_DENSITY_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_population_density")
        print(f"Uploaded {data.num_rows} rows to local_population_density")
        
    save_state("local_population_density", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
