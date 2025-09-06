from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_DEMO@DF_REGION_TYPE_RURB")
    
    if data.num_rows > 0:
        upload_data(data, "urban_rural_demographics")
        print(f"Uploaded {data.num_rows} rows to urban_rural_demographics")
        
    save_state("urban_rural_demographics", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
