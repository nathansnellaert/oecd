from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE3_EMPDC")
    
    if data.num_rows > 0:
        upload_data(data, "employment_by_activity_domestic")
        print(f"Uploaded {data.num_rows} rows to employment_by_activity_domestic")
        
    save_state("employment_by_activity_domestic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
