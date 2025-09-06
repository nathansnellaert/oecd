from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC1@DF_QSA_TRANSACTIONS_D")
    
    if data.num_rows > 0:
        upload_data(data, "quarterly_non_financial_accounts_expenditure")
        print(f"Uploaded {data.num_rows} rows to quarterly_non_financial_accounts_expenditure")
        
    save_state("quarterly_non_financial_accounts_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
