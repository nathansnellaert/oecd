from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV@DF_GOV_2025")
    
    if data.num_rows > 0:
        upload_data(data, "government_at_glance_2025")
        print(f"Uploaded {data.num_rows} rows to government_at_glance_2025")
        
    save_state("government_at_glance_2025", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
