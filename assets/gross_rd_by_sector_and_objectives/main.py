from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDS_GERD@DF_GERD_SEO")
    
    if data.num_rows > 0:
        upload_data(data, "gross_rd_by_sector_and_objectives")
        print(f"Uploaded {data.num_rows} rows to gross_rd_by_sector_and_objectives")
        
    save_state("gross_rd_by_sector_and_objectives", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
