from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PRICES@DF_PRICES_CONTRIB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_inflation_contribution_coicop_1999")
        print(f"Uploaded {data.num_rows} rows to inflation_contribution_coicop_1999")
        
    save_state("inflation_contribution_coicop_1999", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
