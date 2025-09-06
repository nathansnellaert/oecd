from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_MIM")
    
    if data.num_rows > 0:
        upload_data(data, "maternal_infant_mortality")
        print(f"Uploaded {data.num_rows} rows to maternal_infant_mortality")
        
    save_state("maternal_infant_mortality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
