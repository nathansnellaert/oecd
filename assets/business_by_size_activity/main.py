from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDBSBSC_ISIC4@DF_SDBS_ISIC4")
    
    if data.num_rows > 0:
        upload_data(data, "business_by_size_activity")
        print(f"Uploaded {data.num_rows} rows to business_by_size_activity")
        
    save_state("business_by_size_activity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
