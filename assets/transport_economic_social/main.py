from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INDICATORS@DF_ECONOMIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_transport_economic_social")
        print(f"Uploaded {data.num_rows} rows to transport_economic_social")
        
    save_state("transport_economic_social", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
