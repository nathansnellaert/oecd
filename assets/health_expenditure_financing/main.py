from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SHA@DF_SHA")
    
    if data.num_rows > 0:
        upload_data(data, "health_expenditure_financing")
        print(f"Uploaded {data.num_rows} rows to health_expenditure_financing")
        
    save_state("health_expenditure_financing", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
