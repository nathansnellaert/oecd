from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BIBLIO@DF_BIBLIO_COLLAB")
    
    if data.num_rows > 0:
        upload_data(data, "bibliometric_international_collaboration")
        print(f"Uploaded {data.num_rows} rows to bibliometric_international_collaboration")
        
    save_state("bibliometric_international_collaboration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
