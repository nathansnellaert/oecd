from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PII@DF_PUBLIC_INTEGRITY")
    
    if data.num_rows > 0:
        upload_data(data, "public_integrity")
        print(f"Uploaded {data.num_rows} rows to public_integrity")
        
    save_state("public_integrity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
