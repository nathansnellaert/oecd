from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B14")
    
    if data.num_rows > 0:
        upload_data(data, "households_pension_by_informality")
        print(f"Uploaded {data.num_rows} rows to households_pension_by_informality")
        
    save_state("households_pension_by_informality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
