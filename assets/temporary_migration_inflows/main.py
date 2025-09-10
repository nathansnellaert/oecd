from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_MIG_INT@DF_MIG_INT_TEMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_temporary_migration_inflows")
        print(f"Uploaded {data.num_rows} rows to temporary_migration_inflows")
        
    save_state("temporary_migration_inflows", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
