from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DEBT_TRANS_DDOWN@DF_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "debt_transparency_aggregates")
        print(f"Uploaded {data.num_rows} rows to debt_transparency_aggregates")
        
    save_state("debt_transparency_aggregates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
