from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DEO_1@DF_DEO_1")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_development_effectiveness_overview")
        print(f"Uploaded {data.num_rows} rows to development_effectiveness_overview")
        
    save_state("development_effectiveness_overview", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
