from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_PSLC_2022@DF_GOV_PSLC_2022")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_public_service_leadership_capability")
        print(f"Uploaded {data.num_rows} rows to public_service_leadership_capability")
        
    save_state("public_service_leadership_capability", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
