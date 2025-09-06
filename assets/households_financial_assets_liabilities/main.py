from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T7HH_Q")
    
    if data.num_rows > 0:
        upload_data(data, "households_financial_assets_liabilities")
        print(f"Uploaded {data.num_rows} rows to households_financial_assets_liabilities")
        
    save_state("households_financial_assets_liabilities", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
