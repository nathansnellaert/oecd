from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_IPAC@DF_IPAC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ipac_dashboard")
        print(f"Uploaded {data.num_rows} rows to ipac_dashboard")
        
    save_state("ipac_dashboard", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
