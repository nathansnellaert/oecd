from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_EARN_FIELD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_earnings_by_field_of_study")
        print(f"Uploaded {data.num_rows} rows to earnings_by_field_of_study")
        
    save_state("earnings_by_field_of_study", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
