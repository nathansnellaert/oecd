from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PA@DF_PROT_AREA")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_protected_areas")
        print(f"Uploaded {data.num_rows} rows to protected_areas")
        
    save_state("protected_areas", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
