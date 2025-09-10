from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_IPR@DF_QDD_IPR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_intellectual_property_regimes")
        print(f"Uploaded {data.num_rows} rows to intellectual_property_regimes")
        
    save_state("intellectual_property_regimes", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
