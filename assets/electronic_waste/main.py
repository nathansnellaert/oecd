from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EWASTE@DF_EWASTE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_electronic_waste")
        print(f"Uploaded {data.num_rows} rows to electronic_waste")
        
    save_state("electronic_waste", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
