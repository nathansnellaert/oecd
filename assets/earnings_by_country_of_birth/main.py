from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_EARN_REL_NATIVE")
    
    if data.num_rows > 0:
        upload_data(data, "earnings_by_country_of_birth")
        print(f"Uploaded {data.num_rows} rows to earnings_by_country_of_birth")
        
    save_state("earnings_by_country_of_birth", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
