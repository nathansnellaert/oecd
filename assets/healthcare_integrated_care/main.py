from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_IC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_healthcare_integrated_care")
        print(f"Uploaded {data.num_rows} rows to healthcare_integrated_care")
        
    save_state("healthcare_integrated_care", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
