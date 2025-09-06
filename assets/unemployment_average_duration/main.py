from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DUR@DF_AVD_DUR")
    
    if data.num_rows > 0:
        upload_data(data, "unemployment_average_duration")
        print(f"Uploaded {data.num_rows} rows to unemployment_average_duration")
        
    save_state("unemployment_average_duration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
