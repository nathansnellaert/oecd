from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_LTCR@DF_HEALTH_LTCR")
    
    if data.num_rows > 0:
        upload_data(data, "long_term_care_resources")
        print(f"Uploaded {data.num_rows} rows to long_term_care_resources")
        
    save_state("long_term_care_resources", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
