from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG@DF_NAAG_I")
    
    if data.num_rows > 0:
        upload_data(data, "gdp_accounts")
        print(f"Uploaded {data.num_rows} rows to gdp_accounts")
        
    save_state("gdp_accounts", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
