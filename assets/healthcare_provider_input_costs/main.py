from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SHA@DF_SHA_FP")
    
    if data.num_rows > 0:
        upload_data(data, "healthcare_provider_input_costs")
        print(f"Uploaded {data.num_rows} rows to healthcare_provider_input_costs")
        
    save_state("healthcare_provider_input_costs", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
