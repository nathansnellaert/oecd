from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_COASTAL_FLOOD_DDOWN@DF_COASTAL_FLOOD_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "local_coastal_flooding")
        print(f"Uploaded {data.num_rows} rows to local_coastal_flooding")
        
    save_state("local_coastal_flooding", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
