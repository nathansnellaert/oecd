from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDS_GOV@DF_GBARD_NABS07")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_government_budget_allocations_rd")
        print(f"Uploaded {data.num_rows} rows to government_budget_allocations_rd")
        
    save_state("government_budget_allocations_rd", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
