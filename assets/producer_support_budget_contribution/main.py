from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@BP_CGE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_producer_support_budget_contribution")
        print(f"Uploaded {data.num_rows} rows to producer_support_budget_contribution")
        
    save_state("producer_support_budget_contribution", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
