from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIME_USE@DF_TIME_USE")
    
    if data.num_rows > 0:
        upload_data(data, "time_use")
        print(f"Uploaded {data.num_rows} rows to time_use")
        
    save_state("time_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
