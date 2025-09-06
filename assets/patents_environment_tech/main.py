from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PATENTS@DF_PATENTS_ENVIROMENT")
    
    if data.num_rows > 0:
        upload_data(data, "patents_environment_tech")
        print(f"Uploaded {data.num_rows} rows to patents_environment_tech")
        
    save_state("patents_environment_tech", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
