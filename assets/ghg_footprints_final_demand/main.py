from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ICIO_GHG_EXPD@DF_ICIO_GHG_EXPD_2023")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ghg_footprints_final_demand")
        print(f"Uploaded {data.num_rows} rows to ghg_footprints_final_demand")
        
    save_state("ghg_footprints_final_demand", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
