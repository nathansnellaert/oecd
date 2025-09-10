from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_DEMO@DF_MIGR_FLOW")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_migration_flows")
        print(f"Uploaded {data.num_rows} rows to regional_migration_flows")
        
    save_state("regional_migration_flows", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
