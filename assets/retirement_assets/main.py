from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FP@DF_PA")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_retirement_assets")
        print(f"Uploaded {data.num_rows} rows to retirement_assets")
        
    save_state("retirement_assets", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
