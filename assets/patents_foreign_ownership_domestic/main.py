from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PATENTS@DF_PATENTS_FOREIGN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_patents_foreign_ownership_domestic")
        print(f"Uploaded {data.num_rows} rows to patents_foreign_ownership_domestic")
        
    save_state("patents_foreign_ownership_domestic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
