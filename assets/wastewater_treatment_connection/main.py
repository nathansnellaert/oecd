from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WATER_TREAT@DF_WATER_TREAT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_wastewater_treatment_connection")
        print(f"Uploaded {data.num_rows} rows to wastewater_treatment_connection")
        
    save_state("wastewater_treatment_connection", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
