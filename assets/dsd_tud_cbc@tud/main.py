from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TUD_CBC@DF_TUD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_dsd_tud_cbc@tud")
        print(f"Uploaded {data.num_rows} rows to dsd_tud_cbc@tud")
        
    save_state("dsd_tud_cbc@tud", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
