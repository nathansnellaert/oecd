from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_DISCHARGE@DF_WATER_DISCHARGE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_wastewater_generation_discharge")
        print(f"Uploaded {data.num_rows} rows to wastewater_generation_discharge")
        
    save_state("wastewater_generation_discharge", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
