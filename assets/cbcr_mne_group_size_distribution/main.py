from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CBCR@DF_CBCRV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_cbcr_mne_group_size_distribution")
        print(f"Uploaded {data.num_rows} rows to cbcr_mne_group_size_distribution")
        
    save_state("cbcr_mne_group_size_distribution", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
