from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EO@DF_EO")
    
    if data.num_rows > 0:
        upload_data(data, "economic_outlook_117")
        print(f"Uploaded {data.num_rows} rows to economic_outlook_117")
        
    save_state("economic_outlook_117", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
