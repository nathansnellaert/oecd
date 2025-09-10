from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROT@DF_HEALTH_PROT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_healthcare_coverage")
        print(f"Uploaded {data.num_rows} rows to healthcare_coverage")
        
    save_state("healthcare_coverage", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
