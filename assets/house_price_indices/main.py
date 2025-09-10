from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RHPI@DF_RHPI_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_house_price_indices")
        print(f"Uploaded {data.num_rows} rows to house_price_indices")
        
    save_state("house_price_indices", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
