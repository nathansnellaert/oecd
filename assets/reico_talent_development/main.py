from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REICO_FULL@DF_RDT")
    
    if data.num_rows > 0:
        upload_data(data, "reico_talent_development")
        print(f"Uploaded {data.num_rows} rows to reico_talent_development")
        
    save_state("reico_talent_development", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
