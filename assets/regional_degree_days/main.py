from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_CLIM@DF_DEGREE_DAYS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_degree_days")
        print(f"Uploaded {data.num_rows} rows to regional_degree_days")
        
    save_state("regional_degree_days", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
