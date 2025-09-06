from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR@DF_OUTLOOK_2021_2030")
    
    if data.num_rows > 0:
        upload_data(data, "agricultural_outlook_2021_2030")
        print(f"Uploaded {data.num_rows} rows to agricultural_outlook_2021_2030")
        
    save_state("agricultural_outlook_2021_2030", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
