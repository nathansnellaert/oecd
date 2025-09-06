from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B12")
    
    if data.num_rows > 0:
        upload_data(data, "workers_international_poverty_gender_status")
        print(f"Uploaded {data.num_rows} rows to workers_international_poverty_gender_status")
        
    save_state("workers_international_poverty_gender_status", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
