from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_LAB@DF_TYPE_RURB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_labour_by_urban_rural")
        print(f"Uploaded {data.num_rows} rows to labour_by_urban_rural")
        
    save_state("labour_by_urban_rural", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
