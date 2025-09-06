from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_DEMO@DF_DEMO")
    
    if data.num_rows > 0:
        upload_data(data, "regional_demography")
        print(f"Uploaded {data.num_rows} rows to regional_demography")
        
    save_state("regional_demography", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
