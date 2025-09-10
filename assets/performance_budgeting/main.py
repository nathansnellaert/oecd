from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_PERBUD@DF_GOV_PERBUD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_performance_budgeting")
        print(f"Uploaded {data.num_rows} rows to performance_budgeting")
        
    save_state("performance_budgeting", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
