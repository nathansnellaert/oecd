from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sustainable_development_goals")
        print(f"Uploaded {data.num_rows} rows to sustainable_development_goals")
        
    save_state("sustainable_development_goals", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
