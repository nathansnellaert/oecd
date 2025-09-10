from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SUBEMP@DF_SUBEMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_subnational_public_employment")
        print(f"Uploaded {data.num_rows} rows to subnational_public_employment")
        
    save_state("subnational_public_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
