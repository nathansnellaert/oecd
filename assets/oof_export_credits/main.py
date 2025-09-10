from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC2@DF_DAC2B")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_oof_export_credits")
        print(f"Uploaded {data.num_rows} rows to oof_export_credits")
        
    save_state("oof_export_credits", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
