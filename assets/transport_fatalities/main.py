from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ST@DF_STFAT")
    
    if data.num_rows > 0:
        upload_data(data, "transport_fatalities")
        print(f"Uploaded {data.num_rows} rows to transport_fatalities")
        
    save_state("transport_fatalities", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
