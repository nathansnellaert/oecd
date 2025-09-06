from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG@DF_NAAG_II")
    
    if data.num_rows > 0:
        upload_data(data, "national_income")
        print(f"Uploaded {data.num_rows} rows to national_income")
        
    save_state("national_income", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
