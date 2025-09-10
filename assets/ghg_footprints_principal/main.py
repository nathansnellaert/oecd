from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ICIO_GHG_MAIN@DF_ICIO_GHG_MAIN_2023")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ghg_footprints_principal")
        print(f"Uploaded {data.num_rows} rows to ghg_footprints_principal")
        
    save_state("ghg_footprints_principal", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
