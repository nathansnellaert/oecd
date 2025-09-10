from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ICT_B@DF_BUSINESSES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ict_business_usage")
        print(f"Uploaded {data.num_rows} rows to ict_business_usage")
        
    save_state("ict_business_usage", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
