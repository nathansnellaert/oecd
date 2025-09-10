from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC1@DF_DAC5")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_oda_by_sector_provider")
        print(f"Uploaded {data.num_rows} rows to oda_by_sector_provider")
        
    save_state("oda_by_sector_provider", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
