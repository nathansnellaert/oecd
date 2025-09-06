from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG_G_6")
    
    if data.num_rows > 0:
        upload_data(data, "sdg_water_sanitation")
        print(f"Uploaded {data.num_rows} rows to sdg_water_sanitation")
        
    save_state("sdg_water_sanitation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
