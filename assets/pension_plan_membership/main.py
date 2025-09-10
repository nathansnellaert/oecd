from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FP@DF_MB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_pension_plan_membership")
        print(f"Uploaded {data.num_rows} rows to pension_plan_membership")
        
    save_state("pension_plan_membership", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
