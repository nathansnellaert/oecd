from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_C")
    
    if data.num_rows > 0:
        upload_data(data, "cancer")
        print(f"Uploaded {data.num_rows} rows to cancer")
        
    save_state("cancer", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
