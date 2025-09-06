from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIVA_MAINLV@DF_MAINLV")
    
    if data.num_rows > 0:
        upload_data(data, "tiva_principal_levels")
        print(f"Uploaded {data.num_rows} rows to tiva_principal_levels")
        
    save_state("tiva_principal_levels", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
