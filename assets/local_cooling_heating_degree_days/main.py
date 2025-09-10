from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_DEGREE_DAYS_DDOWN@DF_DEGREE_DAYS_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_cooling_heating_degree_days")
        print(f"Uploaded {data.num_rows} rows to local_cooling_heating_degree_days")
        
    save_state("local_cooling_heating_degree_days", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
