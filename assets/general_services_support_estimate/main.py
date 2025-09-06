from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@DF_GSSE")
    
    if data.num_rows > 0:
        upload_data(data, "general_services_support_estimate")
        print(f"Uploaded {data.num_rows} rows to general_services_support_estimate")
        
    save_state("general_services_support_estimate", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
