from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_AFRICA@DF_REV_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_africa_tax_revenues_all_countries")
        print(f"Uploaded {data.num_rows} rows to africa_tax_revenues_all_countries")
        
    save_state("africa_tax_revenues_all_countries", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
