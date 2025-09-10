from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STAN@DF_STAN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_stan_structural_analysis")
        print(f"Uploaded {data.num_rows} rows to stan_structural_analysis")
        
    save_state("stan_structural_analysis", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
