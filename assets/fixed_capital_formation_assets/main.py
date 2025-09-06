from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG@DF_NAAG_III_GFCF")
    
    if data.num_rows > 0:
        upload_data(data, "fixed_capital_formation_assets")
        print(f"Uploaded {data.num_rows} rows to fixed_capital_formation_assets")
        
    save_state("fixed_capital_formation_assets", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
