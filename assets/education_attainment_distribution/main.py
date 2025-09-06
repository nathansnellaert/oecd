from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA")
    
    if data.num_rows > 0:
        upload_data(data, "education_attainment_distribution")
        print(f"Uploaded {data.num_rows} rows to education_attainment_distribution")
        
    save_state("education_attainment_distribution", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
