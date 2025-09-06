from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_OECD@DF_REVCZE")
    
    if data.num_rows > 0:
        upload_data(data, "czechia_tax_revenues")
        print(f"Uploaded {data.num_rows} rows to czechia_tax_revenues")
        
    save_state("czechia_tax_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
