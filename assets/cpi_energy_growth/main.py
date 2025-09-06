from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PRICES@DF_PRICES_N_CP045_0722")
    
    if data.num_rows > 0:
        upload_data(data, "cpi_energy_growth")
        print(f"Uploaded {data.num_rows} rows to cpi_energy_growth")
        
    save_state("cpi_energy_growth", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
