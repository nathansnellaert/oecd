from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10_IDC@DF_TABLE610A_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "annual_financial_accounts_flows_consolidated")
        print(f"Uploaded {data.num_rows} rows to annual_financial_accounts_flows_consolidated")
        
    save_state("annual_financial_accounts_flows_consolidated", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
