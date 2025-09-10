from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ECO@DF_TYPE_METRO")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_metro_economic")
        print(f"Uploaded {data.num_rows} rows to metro_economic")
        
    save_state("metro_economic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
