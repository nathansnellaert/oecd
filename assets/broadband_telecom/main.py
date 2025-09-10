from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BB_DATABASE@DF_BB_TEL_DATABASE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_broadband_telecom")
        print(f"Uploaded {data.num_rows} rows to broadband_telecom")
        
    save_state("broadband_telecom", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
