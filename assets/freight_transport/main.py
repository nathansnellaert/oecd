from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TRENDS@DF_TRENDSFREIGHT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_freight_transport")
        print(f"Uploaded {data.num_rows} rows to freight_transport")
        
    save_state("freight_transport", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
