from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DUR@DF_DUR_D")
    
    if data.num_rows > 0:
        upload_data(data, "unemployment_by_duration")
        print(f"Uploaded {data.num_rows} rows to unemployment_by_duration")
        
    save_state("unemployment_by_duration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
