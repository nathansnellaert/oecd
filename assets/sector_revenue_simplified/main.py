from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE13_REV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sector_revenue_simplified")
        print(f"Uploaded {data.num_rows} rows to sector_revenue_simplified")
        
    save_state("sector_revenue_simplified", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
