from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ST@DF_STFUEL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_motor_fuel_deliveries")
        print(f"Uploaded {data.num_rows} rows to motor_fuel_deliveries")
        
    save_state("motor_fuel_deliveries", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
