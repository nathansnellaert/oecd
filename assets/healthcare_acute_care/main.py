from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_AC")
    
    if data.num_rows > 0:
        upload_data(data, "healthcare_acute_care")
        print(f"Uploaded {data.num_rows} rows to healthcare_acute_care")
        
    save_state("healthcare_acute_care", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
