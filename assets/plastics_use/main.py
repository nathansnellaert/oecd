from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PU@DF_PU")
    
    if data.num_rows > 0:
        upload_data(data, "plastics_use")
        print(f"Uploaded {data.num_rows} rows to plastics_use")
        
    save_state("plastics_use", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
