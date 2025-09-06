from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_UNEMPLOYED")
    
    if data.num_rows > 0:
        upload_data(data, "unemployed_adult_share")
        print(f"Uploaded {data.num_rows} rows to unemployed_adult_share")
        
    save_state("unemployed_adult_share", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
