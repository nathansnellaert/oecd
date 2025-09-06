from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_SOC@DF_VOTER")
    
    if data.num_rows > 0:
        upload_data(data, "regional_civic_engagement")
        print(f"Uploaded {data.num_rows} rows to regional_civic_engagement")
        
    save_state("regional_civic_engagement", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
