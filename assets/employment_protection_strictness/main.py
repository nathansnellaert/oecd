from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EPL@DF_EPL")
    
    if data.num_rows > 0:
        upload_data(data, "employment_protection_strictness")
        print(f"Uploaded {data.num_rows} rows to employment_protection_strictness")
        
    save_state("employment_protection_strictness", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
