from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_ECO@DF_LPR")
    
    if data.num_rows > 0:
        upload_data(data, "regional_labour_productivity")
        print(f"Uploaded {data.num_rows} rows to regional_labour_productivity")
        
    save_state("regional_labour_productivity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
