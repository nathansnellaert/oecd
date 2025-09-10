from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_WT@DF_STA_TCH")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_dsd_eag_wt@sta_tch")
        print(f"Uploaded {data.num_rows} rows to dsd_eag_wt@sta_tch")
        
    save_state("dsd_eag_wt@sta_tch", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
