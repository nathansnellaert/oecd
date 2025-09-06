from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_HGRR@DF_HGRR")
    
    if data.num_rows > 0:
        upload_data(data, "unemployment_benefit_replacement_rates")
        print(f"Uploaded {data.num_rows} rows to unemployment_benefit_replacement_rates")
        
    save_state("unemployment_benefit_replacement_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
