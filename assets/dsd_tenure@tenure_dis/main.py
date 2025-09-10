from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TENURE@DF_TENURE_DIS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_dsd_tenure@tenure_dis")
        print(f"Uploaded {data.num_rows} rows to dsd_tenure@tenure_dis")
        
    save_state("dsd_tenure@tenure_dis", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
