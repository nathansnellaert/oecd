from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DF_SDG_GLC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sdg_country_global")
        print(f"Uploaded {data.num_rows} rows to sdg_country_global")
        
    save_state("sdg_country_global", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
