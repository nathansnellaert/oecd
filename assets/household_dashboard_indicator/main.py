from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HHDASH@DF_HHDASH_INDIC")
    
    if data.num_rows > 0:
        upload_data(data, "household_dashboard_indicator")
        print(f"Uploaded {data.num_rows} rows to household_dashboard_indicator")
        
    save_state("household_dashboard_indicator", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
