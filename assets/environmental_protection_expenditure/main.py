from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EPEA@DF_EPEA")
    
    if data.num_rows > 0:
        upload_data(data, "environmental_protection_expenditure")
        print(f"Uploaded {data.num_rows} rows to environmental_protection_expenditure")
        
    save_state("environmental_protection_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
