from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_TAB16")
    
    if data.num_rows > 0:
        upload_data(data, "afdd_public_finances")
        print(f"Uploaded {data.num_rows} rows to afdd_public_finances")
        
    save_state("afdd_public_finances", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
