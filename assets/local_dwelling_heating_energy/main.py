from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_HOUSING_DDOWN@DF_HEATING_FUEL_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "local_dwelling_heating_energy")
        print(f"Uploaded {data.num_rows} rows to local_dwelling_heating_energy")
        
    save_state("local_dwelling_heating_energy", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
