from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AGR@DF_OUTLOOK_2022_2031")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_agricultural_outlook_2022_2031")
        print(f"Uploaded {data.num_rows} rows to agricultural_outlook_2022_2031")
        
    save_state("agricultural_outlook_2022_2031", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
