from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SBRD@DF_SBRD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_rd_indicators_sub_platform")
        print(f"Uploaded {data.num_rows} rows to rd_indicators_sub_platform")
        
    save_state("rd_indicators_sub_platform", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
