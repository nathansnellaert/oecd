from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PATENTS@DF_PATENTS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_patents_by_technology")
        print(f"Uploaded {data.num_rows} rows to patents_by_technology")
        
    save_state("patents_by_technology", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
