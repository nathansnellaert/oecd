from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_IALFS_WAP_Q")
    
    if data.num_rows > 0:
        upload_data(data, "working_age_population")
        print(f"Uploaded {data.num_rows} rows to working_age_population")
        
    save_state("working_age_population", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
