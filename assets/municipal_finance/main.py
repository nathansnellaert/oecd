from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SNGF_AGG@DF_MUNIFI")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_municipal_finance")
        print(f"Uploaded {data.num_rows} rows to municipal_finance")
        
    save_state("municipal_finance", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
