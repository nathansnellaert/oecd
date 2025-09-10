from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TOURISM_KEY@DF_KEY_IND_PC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_tourism_economic_indicators")
        print(f"Uploaded {data.num_rows} rows to tourism_economic_indicators")
        
    save_state("tourism_economic_indicators", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
