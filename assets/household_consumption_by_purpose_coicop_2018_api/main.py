from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE5A_T500")
    
    if data.num_rows > 0:
        upload_data(data, "household_consumption_by_purpose_coicop_2018_api")
        print(f"Uploaded {data.num_rows} rows to household_consumption_by_purpose_coicop_2018_api")
        
    save_state("household_consumption_by_purpose_coicop_2018_api", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
