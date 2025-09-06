from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FTPT@DF_FTPT_INC_GEN")
    
    if data.num_rows > 0:
        upload_data(data, "parttime_gender_share")
        print(f"Uploaded {data.num_rows} rows to parttime_gender_share")
        
    save_state("parttime_gender_share", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
