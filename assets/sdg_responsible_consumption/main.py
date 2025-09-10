from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG_G_12")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sdg_responsible_consumption")
        print(f"Uploaded {data.num_rows} rows to sdg_responsible_consumption")
        
    save_state("sdg_responsible_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
