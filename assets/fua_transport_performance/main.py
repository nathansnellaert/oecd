from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_TRAN@DF_TRAN_PERF")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_fua_transport_performance")
        print(f"Uploaded {data.num_rows} rows to fua_transport_performance")
        
    save_state("fua_transport_performance", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
