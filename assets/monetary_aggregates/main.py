from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STES@DF_MONAGG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_monetary_aggregates")
        print(f"Uploaded {data.num_rows} rows to monetary_aggregates")
        
    save_state("monetary_aggregates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
