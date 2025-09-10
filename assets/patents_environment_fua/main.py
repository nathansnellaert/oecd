from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FUA_INNOV@DF_PATENTS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_patents_environment_fua")
        print(f"Uploaded {data.num_rows} rows to patents_environment_fua")
        
    save_state("patents_environment_fua", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
