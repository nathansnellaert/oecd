from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_IALFS_UNE_M")
    
    if data.num_rows > 0:
        upload_data(data, "monthly_unemployment_rates")
        print(f"Uploaded {data.num_rows} rows to monthly_unemployment_rates")
        
    save_state("monthly_unemployment_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
