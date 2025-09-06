from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV@DF_GOV_DGOGD_2025")
    
    if data.num_rows > 0:
        upload_data(data, "digital_open_government_2025")
        print(f"Uploaded {data.num_rows} rows to digital_open_government_2025")
        
    save_state("digital_open_government_2025", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
