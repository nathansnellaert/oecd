from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ATR_EUSE@DF_ATR_EUSE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_air_transport_energy_use")
        print(f"Uploaded {data.num_rows} rows to air_transport_energy_use")
        
    save_state("air_transport_energy_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
