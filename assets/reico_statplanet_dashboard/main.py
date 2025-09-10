from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REICO_VIZ@DF_SP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_reico_statplanet_dashboard")
        print(f"Uploaded {data.num_rows} rows to reico_statplanet_dashboard")
        
    save_state("reico_statplanet_dashboard", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
