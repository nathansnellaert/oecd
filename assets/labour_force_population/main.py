from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_IALFS_LF_Q")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_labour_force_population")
        print(f"Uploaded {data.num_rows} rows to labour_force_population")
        
    save_state("labour_force_population", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
