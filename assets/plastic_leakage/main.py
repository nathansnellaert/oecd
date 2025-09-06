from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PL@DF_PL")
    
    if data.num_rows > 0:
        upload_data(data, "plastic_leakage")
        print(f"Uploaded {data.num_rows} rows to plastic_leakage")
        
    save_state("plastic_leakage", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
