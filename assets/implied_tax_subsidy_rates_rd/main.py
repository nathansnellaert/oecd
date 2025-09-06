from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDTAX@DF_RDSUB")
    
    if data.num_rows > 0:
        upload_data(data, "implied_tax_subsidy_rates_rd")
        print(f"Uploaded {data.num_rows} rows to implied_tax_subsidy_rates_rd")
        
    save_state("implied_tax_subsidy_rates_rd", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
