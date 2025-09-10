from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TEMP@DF_TEMP_I")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_temporary_employment_incidence")
        print(f"Uploaded {data.num_rows} rows to temporary_employment_incidence")
        
    save_state("temporary_employment_incidence", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
