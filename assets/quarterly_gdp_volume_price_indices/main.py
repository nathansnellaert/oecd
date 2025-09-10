from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN1@DF_QNA_EXPENDITURE_INDICES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quarterly_gdp_volume_price_indices")
        print(f"Uploaded {data.num_rows} rows to quarterly_gdp_volume_price_indices")
        
    save_state("quarterly_gdp_volume_price_indices", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
