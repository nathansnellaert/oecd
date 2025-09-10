from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ECO_ROPI@DF_GDP_ROPI")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_gdp_ropi_adjusted")
        print(f"Uploaded {data.num_rows} rows to regional_gdp_ropi_adjusted")
        
    save_state("regional_gdp_ropi_adjusted", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
