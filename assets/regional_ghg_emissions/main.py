from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_CLIM@DF_GHG")
    
    if data.num_rows > 0:
        upload_data(data, "regional_ghg_emissions")
        print(f"Uploaded {data.num_rows} rows to regional_ghg_emissions")
        
    save_state("regional_ghg_emissions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
