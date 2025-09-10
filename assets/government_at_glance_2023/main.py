from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV@DF_GOV_2023")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_government_at_glance_2023")
        print(f"Uploaded {data.num_rows} rows to government_at_glance_2023")
        
    save_state("government_at_glance_2023", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
