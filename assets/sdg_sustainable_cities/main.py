from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG_G_11")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sdg_sustainable_cities")
        print(f"Uploaded {data.num_rows} rows to sdg_sustainable_cities")
        
    save_state("sdg_sustainable_cities", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
