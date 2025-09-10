from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_ASAP@DF_REVJPN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_japan_tax_revenues_asia_pacific")
        print(f"Uploaded {data.num_rows} rows to japan_tax_revenues_asia_pacific")
        
    save_state("japan_tax_revenues_asia_pacific", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
