from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_TRANSPORT_DDOWN@DF_COMMUTING_MODE_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_work_transport_mode")
        print(f"Uploaded {data.num_rows} rows to local_work_transport_mode")
        
    save_state("local_work_transport_mode", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
