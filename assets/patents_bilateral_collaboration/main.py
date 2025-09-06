from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PAT_COL@DF_PAT_COL")
    
    if data.num_rows > 0:
        upload_data(data, "patents_bilateral_collaboration")
        print(f"Uploaded {data.num_rows} rows to patents_bilateral_collaboration")
        
    save_state("patents_bilateral_collaboration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
