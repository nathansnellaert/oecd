from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_ASAP@DF_REVNIU")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_new_zealand_tax_revenue_asia_pacific")
        print(f"Uploaded {data.num_rows} rows to new_zealand_tax_revenue_asia_pacific")
        
    save_state("new_zealand_tax_revenue_asia_pacific", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
