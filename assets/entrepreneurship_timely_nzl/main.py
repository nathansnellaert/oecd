from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIE@DF_TIE_NZL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_entrepreneurship_timely_nzl")
        print(f"Uploaded {data.num_rows} rows to entrepreneurship_timely_nzl")
        
    save_state("entrepreneurship_timely_nzl", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
