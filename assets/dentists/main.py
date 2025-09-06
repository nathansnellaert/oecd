from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_REAC_EMP@DF_DNST")
    
    if data.num_rows > 0:
        upload_data(data, "dentists")
        print(f"Uploaded {data.num_rows} rows to dentists")
        
    save_state("dentists", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
