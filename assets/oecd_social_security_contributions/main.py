from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_COMP_OECD@DF_SSCPTOECD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_oecd_social_security_contributions")
        print(f"Uploaded {data.num_rows} rows to oecd_social_security_contributions")
        
    save_state("oecd_social_security_contributions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
