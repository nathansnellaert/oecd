from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TOURISM_EXP@DF_EXPENDITURE")
    
    if data.num_rows > 0:
        upload_data(data, "internal_tourism_consumption")
        print(f"Uploaded {data.num_rows} rows to internal_tourism_consumption")
        
    save_state("internal_tourism_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
