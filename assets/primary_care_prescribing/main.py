from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_PIPC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_primary_care_prescribing")
        print(f"Uploaded {data.num_rows} rows to primary_care_prescribing")
        
    save_state("primary_care_prescribing", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
