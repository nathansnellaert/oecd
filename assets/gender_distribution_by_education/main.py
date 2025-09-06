from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_DISTR_GENDER")
    
    if data.num_rows > 0:
        upload_data(data, "gender_distribution_by_education")
        print(f"Uploaded {data.num_rows} rows to gender_distribution_by_education")
        
    save_state("gender_distribution_by_education", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
