from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INS@DF_CLASSES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_insurance_by_class")
        print(f"Uploaded {data.num_rows} rows to insurance_by_class")
        
    save_state("insurance_by_class", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
