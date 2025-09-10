from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_HEALTH@DF_RISK")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_health_risks")
        print(f"Uploaded {data.num_rows} rows to regional_health_risks")
        
    save_state("regional_health_risks", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
