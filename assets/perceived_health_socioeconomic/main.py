from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_PHS_SES")
    
    if data.num_rows > 0:
        upload_data(data, "perceived_health_socioeconomic")
        print(f"Uploaded {data.num_rows} rows to perceived_health_socioeconomic")
        
    save_state("perceived_health_socioeconomic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
