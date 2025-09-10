from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_SOC@DF_HOUSING")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_housing")
        print(f"Uploaded {data.num_rows} rows to regional_housing")
        
    save_state("regional_housing", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
