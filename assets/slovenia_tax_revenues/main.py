from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_OECD@DF_REVSVN")
    
    if data.num_rows > 0:
        upload_data(data, "slovenia_tax_revenues")
        print(f"Uploaded {data.num_rows} rows to slovenia_tax_revenues")
        
    save_state("slovenia_tax_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
