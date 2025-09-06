from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_AFRICA@DF_REVTCD")
    
    if data.num_rows > 0:
        upload_data(data, "chad_tax_revenues")
        print(f"Uploaded {data.num_rows} rows to chad_tax_revenues")
        
    save_state("chad_tax_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
