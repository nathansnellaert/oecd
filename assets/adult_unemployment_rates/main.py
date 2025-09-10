from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_UNEMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_adult_unemployment_rates")
        print(f"Uploaded {data.num_rows} rows to adult_unemployment_rates")
        
    save_state("adult_unemployment_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
