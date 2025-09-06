from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_NON_FIN_STUD@DF_UOE_NF_DIST_RPTR")
    
    if data.num_rows > 0:
        upload_data(data, "repetition_rate")
        print(f"Uploaded {data.num_rows} rows to repetition_rate")
        
    save_state("repetition_rate", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
