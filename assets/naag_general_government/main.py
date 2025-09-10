from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAAG_VI@DF_NAAG_VI")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_naag_general_government")
        print(f"Uploaded {data.num_rows} rows to naag_general_government")
        
    save_state("naag_general_government", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
