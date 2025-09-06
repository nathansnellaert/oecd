from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DEO_3@DF_DEO_3")
    
    if data.num_rows > 0:
        upload_data(data, "digital_economy_outlook_3")
        print(f"Uploaded {data.num_rows} rows to digital_economy_outlook_3")
        
    save_state("digital_economy_outlook_3", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
