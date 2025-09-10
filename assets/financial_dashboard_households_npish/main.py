from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FIN_DASH@DF_FIN_DASH_S1M")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_financial_dashboard_households_npish")
        print(f"Uploaded {data.num_rows} rows to financial_dashboard_households_npish")
        
    save_state("financial_dashboard_households_npish", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
