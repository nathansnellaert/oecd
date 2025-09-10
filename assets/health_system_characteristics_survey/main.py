from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HSCS@DF_HSCS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_health_system_characteristics_survey")
        print(f"Uploaded {data.num_rows} rows to health_system_characteristics_survey")
        
    save_state("health_system_characteristics_survey", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
