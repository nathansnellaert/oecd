from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T7PSD_Q")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_public_sector_debt_quarterly")
        print(f"Uploaded {data.num_rows} rows to public_sector_debt_quarterly")
        
    save_state("public_sector_debt_quarterly", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
