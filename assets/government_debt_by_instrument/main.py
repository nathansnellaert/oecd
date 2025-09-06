from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PSD_D1D4@DF_PSD_D1D4")
    
    if data.num_rows > 0:
        upload_data(data, "government_debt_by_instrument")
        print(f"Uploaded {data.num_rows} rows to government_debt_by_instrument")
        
    save_state("government_debt_by_instrument", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
