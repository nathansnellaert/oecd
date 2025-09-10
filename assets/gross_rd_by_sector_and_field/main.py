from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDS_GERD@DF_GERD_FORD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gross_rd_by_sector_and_field")
        print(f"Uploaded {data.num_rows} rows to gross_rd_by_sector_and_field")
        
    save_state("gross_rd_by_sector_and_field", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
