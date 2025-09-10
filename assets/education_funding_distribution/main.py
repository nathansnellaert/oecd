from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_UOE_FIN@DF_UOE_FIN_SOURCE_GV_PR_NDOM")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_education_funding_distribution")
        print(f"Uploaded {data.num_rows} rows to education_funding_distribution")
        
    save_state("education_funding_distribution", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
