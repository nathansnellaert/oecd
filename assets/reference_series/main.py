from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG@DF_NAAG_IX")
    
    if data.num_rows > 0:
        upload_data(data, "reference_series")
        print(f"Uploaded {data.num_rows} rows to reference_series")
        
    save_state("reference_series", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
