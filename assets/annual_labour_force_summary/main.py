from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ALFS@DF_SUMTAB")
    
    if data.num_rows > 0:
        upload_data(data, "annual_labour_force_summary")
        print(f"Uploaded {data.num_rows} rows to annual_labour_force_summary")
        
    save_state("annual_labour_force_summary", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
