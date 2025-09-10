from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AN_HOUSE_PRICES@DF_HOUSE_PRICES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_analytical_house_prices")
        print(f"Uploaded {data.num_rows} rows to analytical_house_prices")
        
    save_state("analytical_house_prices", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
