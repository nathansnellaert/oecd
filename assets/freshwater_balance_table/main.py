from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_BALANCE@DF_WATER_BALANCE")
    
    if data.num_rows > 0:
        upload_data(data, "freshwater_balance_table")
        print(f"Uploaded {data.num_rows} rows to freshwater_balance_table")
        
    save_state("freshwater_balance_table", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
