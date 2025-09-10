from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_IALFS_OLF_WAP_Q")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_population_outside_labour_force")
        print(f"Uploaded {data.num_rows} rows to population_outside_labour_force")
        
    save_state("population_outside_labour_force", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
