from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@DF_MONREF")
    
    if data.num_rows > 0:
        upload_data(data, "agriculture_support_estimates")
        print(f"Uploaded {data.num_rows} rows to agriculture_support_estimates")
        
    save_state("agriculture_support_estimates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
