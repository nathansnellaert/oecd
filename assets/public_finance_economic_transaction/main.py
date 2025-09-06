from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_TRANSACTION@DF_GOV_TRANSACTION_2023")
    
    if data.num_rows > 0:
        upload_data(data, "public_finance_economic_transaction")
        print(f"Uploaded {data.num_rows} rows to public_finance_economic_transaction")
        
    save_state("public_finance_economic_transaction", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
