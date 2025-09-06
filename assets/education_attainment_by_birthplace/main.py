from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_EA_MIGR")
    
    if data.num_rows > 0:
        upload_data(data, "education_attainment_by_birthplace")
        print(f"Uploaded {data.num_rows} rows to education_attainment_by_birthplace")
        
    save_state("education_attainment_by_birthplace", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
