from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ST@DF_STREG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_vehicle_registrations")
        print(f"Uploaded {data.num_rows} rows to vehicle_registrations")
        
    save_state("vehicle_registrations", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
