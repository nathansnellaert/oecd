from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RHPI_TARGET@DF_RHPI_TARGET")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_house_price_headline")
        print(f"Uploaded {data.num_rows} rows to house_price_headline")
        
    save_state("house_price_headline", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
