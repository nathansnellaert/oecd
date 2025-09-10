from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_OTHMRKR@DF_OTHERMARKERS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_other_policy_markers")
        print(f"Uploaded {data.num_rows} rows to other_policy_markers")
        
    save_state("other_policy_markers", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
