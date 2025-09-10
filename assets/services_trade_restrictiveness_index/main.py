from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STRI@DF_STRI_MAIN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_services_trade_restrictiveness_index")
        print(f"Uploaded {data.num_rows} rows to services_trade_restrictiveness_index")
        
    save_state("services_trade_restrictiveness_index", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
