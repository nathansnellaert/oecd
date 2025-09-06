from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EARNINGS@AGE_WAGE_GAP")
    
    if data.num_rows > 0:
        upload_data(data, "wage_gap_by_age")
        print(f"Uploaded {data.num_rows} rows to wage_gap_by_age")
        
    save_state("wage_gap_by_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
