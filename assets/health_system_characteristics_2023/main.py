from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HSCS2023@DF_HSCS2023")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_health_system_characteristics_2023")
        print(f"Uploaded {data.num_rows} rows to health_system_characteristics_2023")
        
    save_state("health_system_characteristics_2023", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
