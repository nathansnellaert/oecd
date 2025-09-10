from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SOCX_AGG@DF_PUB_OLD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_public_old_age_survivors_gdp")
        print(f"Uploaded {data.num_rows} rows to public_old_age_survivors_gdp")
        
    save_state("public_old_age_survivors_gdp", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
