from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_ASAP@DF_REVKHM")
    
    if data.num_rows > 0:
        upload_data(data, "cambodia_revenues")
        print(f"Uploaded {data.num_rows} rows to cambodia_revenues")
        
    save_state("cambodia_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
