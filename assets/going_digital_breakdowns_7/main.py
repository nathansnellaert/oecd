from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TOOLKIT_7@DF_GD_BREAKDOWNS_7")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_going_digital_breakdowns_7")
        print(f"Uploaded {data.num_rows} rows to going_digital_breakdowns_7")
        
    save_state("going_digital_breakdowns_7", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
