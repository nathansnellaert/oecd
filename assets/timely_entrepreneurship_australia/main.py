from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIE@DF_TIE_AUS")
    
    if data.num_rows > 0:
        upload_data(data, "timely_entrepreneurship_australia")
        print(f"Uploaded {data.num_rows} rows to timely_entrepreneurship_australia")
        
    save_state("timely_entrepreneurship_australia", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
