from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC2@DF_OFFICIAL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_official_flows")
        print(f"Uploaded {data.num_rows} rows to official_flows")
        
    save_state("official_flows", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
