from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ECO@DF_EMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_employment_by_activity")
        print(f"Uploaded {data.num_rows} rows to regional_employment_by_activity")
        
    save_state("regional_employment_by_activity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
