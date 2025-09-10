from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_IALFS_EMP_Q")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_employment_by_age")
        print(f"Uploaded {data.num_rows} rows to employment_by_age")
        
    save_state("employment_by_age", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
