from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PU_2019@DF_PU_2019")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_plastics_use_2019")
        print(f"Uploaded {data.num_rows} rows to plastics_use_2019")
        
    save_state("plastics_use_2019", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
