from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_ASAP@DF_REVKOR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_korea_tax_revenues_asia_pacific")
        print(f"Uploaded {data.num_rows} rows to korea_tax_revenues_asia_pacific")
        
    save_state("korea_tax_revenues_asia_pacific", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
