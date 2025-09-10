from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ENV@DF_WASTE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_waste_treatment_regions")
        print(f"Uploaded {data.num_rows} rows to waste_treatment_regions")
        
    save_state("waste_treatment_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
