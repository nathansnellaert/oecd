from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PATENTS@DF_PATENTS_WIPO")
    
    if data.num_rows > 0:
        upload_data(data, "patents_wipo_domains")
        print(f"Uploaded {data.num_rows} rows to patents_wipo_domains")
        
    save_state("patents_wipo_domains", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
