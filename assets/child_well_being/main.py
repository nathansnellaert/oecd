from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CWB@DF_CWB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_child_well_being")
        print(f"Uploaded {data.num_rows} rows to child_well_being")
        
    save_state("child_well_being", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
