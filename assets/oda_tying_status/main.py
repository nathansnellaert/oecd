from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC1@DF_DAC7B")
    
    if data.num_rows > 0:
        upload_data(data, "oda_tying_status")
        print(f"Uploaded {data.num_rows} rows to oda_tying_status")
        
    save_state("oda_tying_status", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
