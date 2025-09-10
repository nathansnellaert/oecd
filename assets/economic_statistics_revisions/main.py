from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STES_REVISIONS@DF_STES_REVISIONS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_economic_statistics_revisions")
        print(f"Uploaded {data.num_rows} rows to economic_statistics_revisions")
        
    save_state("economic_statistics_revisions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
