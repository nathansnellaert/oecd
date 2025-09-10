from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SNG_WOFI@DF_FINANCE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_subnational_finance_debt")
        print(f"Uploaded {data.num_rows} rows to subnational_finance_debt")
        
    save_state("subnational_finance_debt", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
