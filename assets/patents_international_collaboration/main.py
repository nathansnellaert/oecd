from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PAT_COL_RATES@DF_PAT_COL_RATES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_patents_international_collaboration")
        print(f"Uploaded {data.num_rows} rows to patents_international_collaboration")
        
    save_state("patents_international_collaboration", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
