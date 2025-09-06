from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDS_GERD@DF_GERD_SOF")
    
    if data.num_rows > 0:
        upload_data(data, "rd_expenditure_by_sector_and_source")
        print(f"Uploaded {data.num_rows} rows to rd_expenditure_by_sector_and_source")
        
    save_state("rd_expenditure_by_sector_and_source", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
