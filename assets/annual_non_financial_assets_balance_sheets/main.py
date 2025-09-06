from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10_IDC@DF_TABLE9B_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "annual_non_financial_assets_balance_sheets")
        print(f"Uploaded {data.num_rows} rows to annual_non_financial_assets_balance_sheets")
        
    save_state("annual_non_financial_assets_balance_sheets", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
