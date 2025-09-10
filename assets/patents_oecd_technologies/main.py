from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PATENTS@DF_PATENTS_OECDSPECIFIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_patents_oecd_technologies")
        print(f"Uploaded {data.num_rows} rows to patents_oecd_technologies")
        
    save_state("patents_oecd_technologies", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
