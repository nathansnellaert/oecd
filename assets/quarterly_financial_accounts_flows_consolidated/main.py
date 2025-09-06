from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10_IDC@DF_TABLE610Q_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "quarterly_financial_accounts_flows_consolidated")
        print(f"Uploaded {data.num_rows} rows to quarterly_financial_accounts_flows_consolidated")
        
    save_state("quarterly_financial_accounts_flows_consolidated", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
