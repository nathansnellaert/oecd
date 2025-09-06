from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_PIT@DF_PIT_CENT")
    
    if data.num_rows > 0:
        upload_data(data, "pit_central_gov_rates")
        print(f"Uploaded {data.num_rows} rows to pit_central_gov_rates")
        
    save_state("pit_central_gov_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
