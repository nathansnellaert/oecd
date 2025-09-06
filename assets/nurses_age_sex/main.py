from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_REAC_EMP@DF_NURS_AGE_SEX")
    
    if data.num_rows > 0:
        upload_data(data, "nurses_age_sex")
        print(f"Uploaded {data.num_rows} rows to nurses_age_sex")
        
    save_state("nurses_age_sex", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
