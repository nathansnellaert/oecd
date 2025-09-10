from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LFS@DF_LFS_INDIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_employment_unemployment_indicators")
        print(f"Uploaded {data.num_rows} rows to employment_unemployment_indicators")
        
    save_state("employment_unemployment_indicators", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
