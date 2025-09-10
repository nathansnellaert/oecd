from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GHG_PLC_P@DF_GHG_PLC_P")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ghg_emissions_plastic_projections")
        print(f"Uploaded {data.num_rows} rows to ghg_emissions_plastic_projections")
        
    save_state("ghg_emissions_plastic_projections", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
