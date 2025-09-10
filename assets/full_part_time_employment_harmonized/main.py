from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FTPT@DF_FTPT_COMMON")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_full_part_time_employment_harmonized")
        print(f"Uploaded {data.num_rows} rows to full_part_time_employment_harmonized")
        
    save_state("full_part_time_employment_harmonized", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
