from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAPENS_IDC@DF_TABLE29_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "pensions_international_transfer")
        print(f"Uploaded {data.num_rows} rows to pensions_international_transfer")
        
    save_state("pensions_international_transfer", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
