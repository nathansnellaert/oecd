from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_SOC@DF_BROADBAND")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_broadband_access")
        print(f"Uploaded {data.num_rows} rows to regional_broadband_access")
        
    save_state("regional_broadband_access", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
