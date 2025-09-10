from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PPFD@DF_PPFD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_private_philanthropy_development")
        print(f"Uploaded {data.num_rows} rows to private_philanthropy_development")
        
    save_state("private_philanthropy_development", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
