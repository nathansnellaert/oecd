from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_IALFS_UNE_Q")
    
    if data.num_rows > 0:
        upload_data(data, "unemployed_population")
        print(f"Uploaded {data.num_rows} rows to unemployed_population")
        
    save_state("unemployed_population", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
