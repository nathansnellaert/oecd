from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDS_PERS@DF_PERS_FORD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_rd_personnel_by_sector_and_field")
        print(f"Uploaded {data.num_rows} rows to rd_personnel_by_sector_and_field")
        
    save_state("rd_personnel_by_sector_and_field", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
