from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BIBLIO@DF_BIBLIO")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_bibliometric_by_field")
        print(f"Uploaded {data.num_rows} rows to bibliometric_by_field")
        
    save_state("bibliometric_by_field", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
