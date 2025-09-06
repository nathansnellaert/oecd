from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TUD_CBC@DF_CBC")
    
    if data.num_rows > 0:
        upload_data(data, "dsd_tud_cbc@cbc")
        print(f"Uploaded {data.num_rows} rows to dsd_tud_cbc@cbc")
        
    save_state("dsd_tud_cbc@cbc", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
