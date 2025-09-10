from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_AGGHGSEM")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_agricultural_ghg_emissions")
        print(f"Uploaded {data.num_rows} rows to agricultural_ghg_emissions")
        
    save_state("agricultural_ghg_emissions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
