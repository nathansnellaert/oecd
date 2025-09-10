from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GREQ@DF_CRS_GREQ")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_crs_grant_equivalent")
        print(f"Uploaded {data.num_rows} rows to crs_grant_equivalent")
        
    save_state("crs_grant_equivalent", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
