from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE12_EMPDC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_annual_government_employment")
        print(f"Uploaded {data.num_rows} rows to annual_government_employment")
        
    save_state("annual_government_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
