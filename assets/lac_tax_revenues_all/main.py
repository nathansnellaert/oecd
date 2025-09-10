from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_LAC@DF_REV_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_lac_tax_revenues_all")
        print(f"Uploaded {data.num_rows} rows to lac_tax_revenues_all")
        
    save_state("lac_tax_revenues_all", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
