from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PAT_DEV@DF_PAT_DEV")
    
    if data.num_rows > 0:
        upload_data(data, "patents_technology_development")
        print(f"Uploaded {data.num_rows} rows to patents_technology_development")
        
    save_state("patents_technology_development", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
