from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TOURISM_DOM@DF_DOMESTIC")
    
    if data.num_rows > 0:
        upload_data(data, "domestic_tourism")
        print(f"Uploaded {data.num_rows} rows to domestic_tourism")
        
    save_state("domestic_tourism", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
