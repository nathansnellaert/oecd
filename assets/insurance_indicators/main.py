from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INS@DF_IND")
    
    if data.num_rows > 0:
        upload_data(data, "insurance_indicators")
        print(f"Uploaded {data.num_rows} rows to insurance_indicators")
        
    save_state("insurance_indicators", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
