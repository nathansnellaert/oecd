from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INDICATORS@DF_ENVIRONMENT")
    
    if data.num_rows > 0:
        upload_data(data, "transport_energy_environment")
        print(f"Uploaded {data.num_rows} rows to transport_energy_environment")
        
    save_state("transport_energy_environment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
