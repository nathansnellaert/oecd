from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_INDICATOR")
    
    if data.num_rows > 0:
        upload_data(data, "supply_use_table_indicators")
        print(f"Uploaded {data.num_rows} rows to supply_use_table_indicators")
        
    save_state("supply_use_table_indicators", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
