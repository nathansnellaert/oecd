from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_EMP_REAC@DF_PHYS_CAT")
    
    if data.num_rows > 0:
        upload_data(data, "physicians_categories")
        print(f"Uploaded {data.num_rows} rows to physicians_categories")
        
    save_state("physicians_categories", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
