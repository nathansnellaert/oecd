from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TOOLKIT@DF_GD_DISTANCES")
    
    if data.num_rows > 0:
        upload_data(data, "going_digital_country_pages")
        print(f"Uploaded {data.num_rows} rows to going_digital_country_pages")
        
    save_state("going_digital_country_pages", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
