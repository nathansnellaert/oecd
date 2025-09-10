from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_IA@DF_IA")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_minimum_income_benefit_adequacy")
        print(f"Uploaded {data.num_rows} rows to minimum_income_benefit_adequacy")
        
    save_state("minimum_income_benefit_adequacy", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
