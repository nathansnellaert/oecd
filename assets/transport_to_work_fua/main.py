from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_TRAN@DF_TRAN_COMMUT")
    
    if data.num_rows > 0:
        upload_data(data, "transport_to_work_fua")
        print(f"Uploaded {data.num_rows} rows to transport_to_work_fua")
        
    save_state("transport_to_work_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
