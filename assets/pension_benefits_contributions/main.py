from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FP@DF_BC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_pension_benefits_contributions")
        print(f"Uploaded {data.num_rows} rows to pension_benefits_contributions")
        
    save_state("pension_benefits_contributions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
