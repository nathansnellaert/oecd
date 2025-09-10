from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_MIG_INT@DF_MIG_INT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_harmonised_migration_flows")
        print(f"Uploaded {data.num_rows} rows to harmonised_migration_flows")
        
    save_state("harmonised_migration_flows", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
