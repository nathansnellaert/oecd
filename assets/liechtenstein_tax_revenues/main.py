from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_GLOBAL@DF_REVLIE")
    
    if data.num_rows > 0:
        upload_data(data, "liechtenstein_tax_revenues")
        print(f"Uploaded {data.num_rows} rows to liechtenstein_tax_revenues")
        
    save_state("liechtenstein_tax_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
