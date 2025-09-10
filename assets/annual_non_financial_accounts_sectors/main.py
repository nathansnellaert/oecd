from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10_IDC@DF_TABLE14_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_annual_non_financial_accounts_sectors")
        print(f"Uploaded {data.num_rows} rows to annual_non_financial_accounts_sectors")
        
    save_state("annual_non_financial_accounts_sectors", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
