from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_LAB@DF_TYPE_METRO")
    
    if data.num_rows > 0:
        upload_data(data, "labour_by_city_access")
        print(f"Uploaded {data.num_rows} rows to labour_by_city_access")
        
    save_state("labour_by_city_access", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
