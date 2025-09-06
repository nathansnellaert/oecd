from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_LVNG@DF_HEALTH_LVNG")
    
    if data.num_rows > 0:
        upload_data(data, "health_risk_factors")
        print(f"Uploaded {data.num_rows} rows to health_risk_factors")
        
    save_state("health_risk_factors", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
