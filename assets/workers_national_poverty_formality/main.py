from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B11")
    
    if data.num_rows > 0:
        upload_data(data, "workers_national_poverty_formality")
        print(f"Uploaded {data.num_rows} rows to workers_national_poverty_formality")
        
    save_state("workers_national_poverty_formality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
