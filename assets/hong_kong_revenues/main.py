from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_ASAP@DF_REVHKG")
    
    if data.num_rows > 0:
        upload_data(data, "hong_kong_revenues")
        print(f"Uploaded {data.num_rows} rows to hong_kong_revenues")
        
    save_state("hong_kong_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
