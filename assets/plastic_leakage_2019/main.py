from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PL_2019@DF_PL_2019")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_plastic_leakage_2019")
        print(f"Uploaded {data.num_rows} rows to plastic_leakage_2019")
        
    save_state("plastic_leakage_2019", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
