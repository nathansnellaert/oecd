from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_HOURSPOV@DF_HOURSPOV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_work_hours_to_escape_poverty")
        print(f"Uploaded {data.num_rows} rows to work_hours_to_escape_poverty")
        
    save_state("work_hours_to_escape_poverty", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
