from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR_POLIND@DF_COMGSSE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_general_services_support_composition")
        print(f"Uploaded {data.num_rows} rows to general_services_support_composition")
        
    save_state("general_services_support_composition", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
