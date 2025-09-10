from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_SHARE_RPTR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_repeaters_by_gender_level")
        print(f"Uploaded {data.num_rows} rows to repeaters_by_gender_level")
        
    save_state("repeaters_by_gender_level", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
