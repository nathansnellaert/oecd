from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10_IDC@DF_PSD_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_quarterly_public_sector_debt")
        print(f"Uploaded {data.num_rows} rows to quarterly_public_sector_debt")
        
    save_state("quarterly_public_sector_debt", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
