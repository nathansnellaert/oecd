from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AIR_EMISSIONS@DF_AIR_EMISSIONS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_air_emissions")
        print(f"Uploaded {data.num_rows} rows to air_emissions")
        
    save_state("air_emissions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
