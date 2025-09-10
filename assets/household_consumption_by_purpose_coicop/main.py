from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE5_T501")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_household_consumption_by_purpose_coicop")
        print(f"Uploaded {data.num_rows} rows to household_consumption_by_purpose_coicop")
        
    save_state("household_consumption_by_purpose_coicop", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
