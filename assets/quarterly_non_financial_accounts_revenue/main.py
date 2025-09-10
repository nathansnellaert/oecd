from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC1@DF_QSA_TRANSACTIONS_C")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quarterly_non_financial_accounts_revenue")
        print(f"Uploaded {data.num_rows} rows to quarterly_non_financial_accounts_revenue")
        
    save_state("quarterly_non_financial_accounts_revenue", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
