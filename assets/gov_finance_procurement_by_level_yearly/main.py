from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_LEVEL@DF_GOV_LEVEL_YU")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gov_finance_procurement_by_level_yearly")
        print(f"Uploaded {data.num_rows} rows to gov_finance_procurement_by_level_yearly")
        
    save_state("gov_finance_procurement_by_level_yearly", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
