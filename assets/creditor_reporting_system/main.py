from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CRS@DF_CRS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_creditor_reporting_system")
        print(f"Uploaded {data.num_rows} rows to creditor_reporting_system")
        
    save_state("creditor_reporting_system", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
