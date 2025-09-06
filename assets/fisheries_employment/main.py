from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FISH_EMP@DF_FISH_EMPL")
    
    if data.num_rows > 0:
        upload_data(data, "fisheries_employment")
        print(f"Uploaded {data.num_rows} rows to fisheries_employment")
        
    save_state("fisheries_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
