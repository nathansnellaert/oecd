from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SHA@DF_SHA_HK")
    
    if data.num_rows > 0:
        upload_data(data, "healthcare_capital_formation")
        print(f"Uploaded {data.num_rows} rows to healthcare_capital_formation")
        
    save_state("healthcare_capital_formation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
