from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_PIT@DF_PIT_MR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_pit_ssc_marginal_rates")
        print(f"Uploaded {data.num_rows} rows to pit_ssc_marginal_rates")
        
    save_state("pit_ssc_marginal_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
