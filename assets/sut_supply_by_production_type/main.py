from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_SUPPLYP1_T1500")
    
    if data.num_rows > 0:
        upload_data(data, "sut_supply_by_production_type")
        print(f"Uploaded {data.num_rows} rows to sut_supply_by_production_type")
        
    save_state("sut_supply_by_production_type", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
