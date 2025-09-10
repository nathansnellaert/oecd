from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_COM")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_mortality_causes")
        print(f"Uploaded {data.num_rows} rows to mortality_causes")
        
    save_state("mortality_causes", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
