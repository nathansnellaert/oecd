from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN1@DF_QNA_EXPENDITURE_GFCF_SECTOR")
    
    if data.num_rows > 0:
        upload_data(data, "quarterly_gfcf_by_sector")
        print(f"Uploaded {data.num_rows} rows to quarterly_gfcf_by_sector")
        
    save_state("quarterly_gfcf_by_sector", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
