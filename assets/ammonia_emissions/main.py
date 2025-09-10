from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_AGAMMO")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ammonia_emissions")
        print(f"Uploaded {data.num_rows} rows to ammonia_emissions")
        
    save_state("ammonia_emissions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
