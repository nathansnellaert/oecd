from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FIN_DASH@DF_7II_INDIC")
    
    if data.num_rows > 0:
        upload_data(data, "institutional_investors_indicators")
        print(f"Uploaded {data.num_rows} rows to institutional_investors_indicators")
        
    save_state("institutional_investors_indicators", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
