from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FOREST@DF_FOREST")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_forest_use_intensity")
        print(f"Uploaded {data.num_rows} rows to forest_use_intensity")
        
    save_state("forest_use_intensity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
