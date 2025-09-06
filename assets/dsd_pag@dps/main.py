from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PAG@DF_DPS")
    
    if data.num_rows > 0:
        upload_data(data, "dsd_pag@dps")
        print(f"Uploaded {data.num_rows} rows to dsd_pag@dps")
        
    save_state("dsd_pag@dps", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
