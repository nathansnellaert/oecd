from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TRENDS@DF_TRENDS")
    
    if data.num_rows > 0:
        upload_data(data, "transport_trends")
        print(f"Uploaded {data.num_rows} rows to transport_trends")
        
    save_state("transport_trends", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
