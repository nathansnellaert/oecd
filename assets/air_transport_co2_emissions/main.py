from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AIR_TRANSPORT@DF_AIR_TRANSPORT")
    
    if data.num_rows > 0:
        upload_data(data, "air_transport_co2_emissions")
        print(f"Uploaded {data.num_rows} rows to air_transport_co2_emissions")
        
    save_state("air_transport_co2_emissions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
