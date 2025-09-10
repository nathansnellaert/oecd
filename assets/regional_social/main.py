from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_SOC@DF_SOC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_social")
        print(f"Uploaded {data.num_rows} rows to regional_social")
        
    save_state("regional_social", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
