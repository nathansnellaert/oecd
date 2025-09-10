from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_LABOUR@DF_LAB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_labour_api")
        print(f"Uploaded {data.num_rows} rows to regional_labour_api")
        
    save_state("regional_labour_api", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
