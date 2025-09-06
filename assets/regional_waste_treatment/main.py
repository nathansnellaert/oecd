from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_MW@DF_WASTE")
    
    if data.num_rows > 0:
        upload_data(data, "regional_waste_treatment")
        print(f"Uploaded {data.num_rows} rows to regional_waste_treatment")
        
    save_state("regional_waste_treatment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
