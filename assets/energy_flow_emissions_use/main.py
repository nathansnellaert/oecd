from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PEFA@DF_PEFAERUSE")
    
    if data.num_rows > 0:
        upload_data(data, "energy_flow_emissions_use")
        print(f"Uploaded {data.num_rows} rows to energy_flow_emissions_use")
        
    save_state("energy_flow_emissions_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
