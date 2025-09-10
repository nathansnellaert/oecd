from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PAG@DF_IPOP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_dsd_pag@ipop")
        print(f"Uploaded {data.num_rows} rows to dsd_pag@ipop")
        
    save_state("dsd_pag@ipop", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
