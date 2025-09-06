from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STAN@DF_STAN_2025")
    
    if data.num_rows > 0:
        upload_data(data, "stan_structural_analysis_2025")
        print(f"Uploaded {data.num_rows} rows to stan_structural_analysis_2025")
        
    save_state("stan_structural_analysis_2025", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
