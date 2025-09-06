from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DASHBOARD@DEBT")
    
    if data.num_rows > 0:
        upload_data(data, "subnational_budget_balance_debt")
        print(f"Uploaded {data.num_rows} rows to subnational_budget_balance_debt")
        
    save_state("subnational_budget_balance_debt", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
