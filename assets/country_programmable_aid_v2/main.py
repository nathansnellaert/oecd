from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC2@DF_CPA")
    
    if data.num_rows > 0:
        upload_data(data, "country_programmable_aid_v2")
        print(f"Uploaded {data.num_rows} rows to country_programmable_aid_v2")
        
    save_state("country_programmable_aid_v2", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
