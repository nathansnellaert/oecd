from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DUR@DF_DUR_I")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_unemployment_incidence_by_duration")
        print(f"Uploaded {data.num_rows} rows to unemployment_incidence_by_duration")
        
    save_state("unemployment_incidence_by_duration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
