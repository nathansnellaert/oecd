from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG_G_3")
    
    if data.num_rows > 0:
        upload_data(data, "sdg_health_wellbeing")
        print(f"Uploaded {data.num_rows} rows to sdg_health_wellbeing")
        
    save_state("sdg_health_wellbeing", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
