from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_FMR@DF_GOV_FMR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_financial_management_reporting")
        print(f"Uploaded {data.num_rows} rows to financial_management_reporting")
        
    save_state("financial_management_reporting", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
