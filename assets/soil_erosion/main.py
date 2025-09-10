from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGRI_ENV@DF_AGSE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_soil_erosion")
        print(f"Uploaded {data.num_rows} rows to soil_erosion")
        
    save_state("soil_erosion", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
