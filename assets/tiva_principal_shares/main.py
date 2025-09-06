from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIVA_MAINSH@DF_MAINSH")
    
    if data.num_rows > 0:
        upload_data(data, "tiva_principal_shares")
        print(f"Uploaded {data.num_rows} rows to tiva_principal_shares")
        
    save_state("tiva_principal_shares", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
