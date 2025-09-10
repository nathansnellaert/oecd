from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DASHBOARD@INV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_subnational_investment")
        print(f"Uploaded {data.num_rows} rows to subnational_investment")
        
    save_state("subnational_investment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
