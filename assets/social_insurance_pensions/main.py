from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAPENS@DF_TABLE29")
    
    if data.num_rows > 0:
        upload_data(data, "social_insurance_pensions")
        print(f"Uploaded {data.num_rows} rows to social_insurance_pensions")
        
    save_state("social_insurance_pensions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
