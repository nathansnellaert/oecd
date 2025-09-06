from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STRI@DF_STRI_DIGITAL")
    
    if data.num_rows > 0:
        upload_data(data, "digital_services_trade_restrictiveness")
        print(f"Uploaded {data.num_rows} rows to digital_services_trade_restrictiveness")
        
    save_state("digital_services_trade_restrictiveness", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
