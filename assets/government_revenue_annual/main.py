from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE12_REV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_government_revenue_annual")
        print(f"Uploaded {data.num_rows} rows to government_revenue_annual")
        
    save_state("government_revenue_annual", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
