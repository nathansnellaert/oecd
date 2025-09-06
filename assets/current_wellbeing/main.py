from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HSL@DF_HSL_CWB")
    
    if data.num_rows > 0:
        upload_data(data, "current_wellbeing")
        print(f"Uploaded {data.num_rows} rows to current_wellbeing")
        
    save_state("current_wellbeing", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
