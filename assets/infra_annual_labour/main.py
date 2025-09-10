from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_IALFS_INDIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_infra_annual_labour")
        print(f"Uploaded {data.num_rows} rows to infra_annual_labour")
        
    save_state("infra_annual_labour", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
