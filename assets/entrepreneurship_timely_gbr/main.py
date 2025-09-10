from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIE@DF_TIE_GBR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_entrepreneurship_timely_gbr")
        print(f"Uploaded {data.num_rows} rows to entrepreneurship_timely_gbr")
        
    save_state("entrepreneurship_timely_gbr", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
