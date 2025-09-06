from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_DEMO@DF_DEPEND")
    
    if data.num_rows > 0:
        upload_data(data, "regional_dependency_rates")
        print(f"Uploaded {data.num_rows} rows to regional_dependency_rates")
        
    save_state("regional_dependency_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
