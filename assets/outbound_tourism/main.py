from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TOURISM_INTER@DF_OUTBOUND")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_outbound_tourism")
        print(f"Uploaded {data.num_rows} rows to outbound_tourism")
        
    save_state("outbound_tourism", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
