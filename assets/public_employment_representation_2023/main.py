from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV@DF_GOV_EMPPS_REP_2023")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_public_employment_representation_2023")
        print(f"Uploaded {data.num_rows} rows to public_employment_representation_2023")
        
    save_state("public_employment_representation_2023", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
