from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_CLIM@DF_HEAT_STRESS")
    
    if data.num_rows > 0:
        upload_data(data, "regional_heat_stress")
        print(f"Uploaded {data.num_rows} rows to regional_heat_stress")
        
    save_state("regional_heat_stress", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
