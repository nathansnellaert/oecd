from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_EMP_REAC@DF_REAC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_healthcare_human_resources")
        print(f"Uploaded {data.num_rows} rows to healthcare_human_resources")
        
    save_state("healthcare_human_resources", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
