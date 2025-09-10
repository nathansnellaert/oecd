from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_INDICATOR_P7_TS_O")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sut_imports_total_supply_share")
        print(f"Uploaded {data.num_rows} rows to sut_imports_total_supply_share")
        
    save_state("sut_imports_total_supply_share", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
