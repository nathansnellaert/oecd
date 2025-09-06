from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ECO@DF_TRAD")
    
    if data.num_rows > 0:
        upload_data(data, "regional_trade")
        print(f"Uploaded {data.num_rows} rows to regional_trade")
        
    save_state("regional_trade", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
